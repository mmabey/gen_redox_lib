"""Acquire the Redox JSON schema bundle.

Redox publishes the ``schema v4`` bundle at a stable, public URL (the same file
the dashboard's "Dev tool downloads" links to). ``--force-download`` fetches a
fresh copy from there and refreshes the pinned copy vendored in this repo
(``gen_redox_lib/vendor/schemas.zip``), which is otherwise used as-is so
generation and tests never depend on the network.
"""

import shutil
from pathlib import Path
from zipfile import BadZipFile, ZipFile

import click
import requests
from requests import HTTPError
from retry import retry

from .utils import rmrf

VENDORED_SPEC = Path(__file__).resolve().parent.parent / "vendor" / "schemas.zip"
DEFAULT_SPEC_URL = "https://data-models.prod.redoxengine.com/downloads/schemas.zip"


def download_and_extract(
    working_dir: Path,
    *,
    force_download: bool = False,
    spec_url: str = DEFAULT_SPEC_URL,
) -> Path:
    """Put a ``schemas`` directory in ``working_dir`` and return its path.

    Uses the vendored bundle unless ``force_download`` is set, in which case it
    fetches ``spec_url`` and refreshes the vendored copy on success.
    """
    working_dir.mkdir(parents=True, exist_ok=True)
    spec_zip = working_dir / "schemas.zip"

    if force_download:
        _download(spec_url, spec_zip)
        _refresh_vendored_copy(spec_zip)
    else:
        if not VENDORED_SPEC.exists():
            msg = f"No vendored schema bundle at {VENDORED_SPEC} and --force-download not set."
            raise click.UsageError(msg)
        click.echo(f"Using vendored schema bundle: {VENDORED_SPEC}")
        shutil.copyfile(VENDORED_SPEC, spec_zip)

    return _extract(spec_zip)


@retry(HTTPError, tries=10, delay=2, backoff=1.5)
def _download(spec_url: str, spec_zip: Path) -> None:
    click.echo(f"Downloading Redox schema bundle from {spec_url} ...", nl=False)
    resp = requests.get(spec_url, headers={"Accept-Encoding": "gzip, deflate, br"}, timeout=60)
    try:
        resp.raise_for_status()
    except HTTPError:
        click.echo(f" error (HTTP {resp.status_code})")
        raise
    spec_zip.write_bytes(resp.content)
    click.echo(" done")


def _refresh_vendored_copy(spec_zip: Path) -> None:
    try:
        with ZipFile(spec_zip) as zf:
            if zf.testzip() is not None:
                raise BadZipFile
    except BadZipFile:
        click.echo("Downloaded file is not a valid zip; keeping the existing vendored copy.")
        return
    VENDORED_SPEC.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(spec_zip, VENDORED_SPEC)
    click.echo(f"Refreshed vendored schema bundle at {VENDORED_SPEC}")


def _extract(spec_zip: Path) -> Path:
    dst_dir = spec_zip.parent / "schemas"
    if dst_dir.exists():
        rmrf(dst_dir)
    dst_dir.mkdir()
    (dst_dir / "__init__.py").touch()

    click.echo("Unzipping schema bundle")
    try:
        with ZipFile(spec_zip, "r") as zippy:
            zippy.extractall(path=dst_dir)
    except BadZipFile:
        click.echo("Unable to read the zip file contents - the download was likely corrupted.")
        raise

    return dst_dir
