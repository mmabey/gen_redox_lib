from collections.abc import Iterator
from contextlib import contextmanager
from os import chdir
from pathlib import Path


@contextmanager
def temp_chdir(path: str | Path) -> Iterator[None]:
    """Temporarily change the working directory."""
    previous_wd = Path.cwd()
    chdir(Path(path).resolve())
    try:
        yield
    finally:
        chdir(previous_wd)
