from pathlib import Path

import pytest
from click.testing import CliRunner
from tomlkit import parse

import gen_redox_lib
from gen_redox_lib.generate import main as generate_main

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_version():
    assert gen_redox_lib.__version__ == "1.1.0"


def test_pyproject_version():
    pyproject = parse((REPO_ROOT / "pyproject.toml").read_text())
    assert pyproject["project"]["version"] == gen_redox_lib.__version__, (
        "pyproject.toml [project].version differs from gen_redox_lib.__version__"
    )


@pytest.fixture
def fresh_lib_generation(tmp_path: Path) -> Path:
    """Generate the redox library from the vendored schema bundle."""
    dst = tmp_path / "redox" / "redox"
    dst.mkdir(parents=True)
    result = CliRunner().invoke(generate_main, ["--dst", str(dst)], catch_exceptions=False)
    assert result.exit_code == 0, result.output
    return dst


def test_compare_generated_with_existing(snapshot, fresh_lib_generation: Path):
    snapshot.snapshot_dir = Path(__file__).parent.resolve() / "snapshots"
    generated_root = fresh_lib_generation
    for f in sorted(generated_root.glob("**/*.py")):
        try:
            snapshot.assert_match(
                value=f.read_text(),
                snapshot_name=snapshot.snapshot_dir / f.relative_to(generated_root),
            )
        except AssertionError:
            print("Snapshot mismatch - run `./update_snapshots.sh` if this is expected.")  # noqa: T201
            print(f"FAILED: {f}")  # noqa: T201
            raise
