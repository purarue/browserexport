from pathlib import Path
from sqlite3 import Connection

PathIsh = str | Path
# a path or a connection to a database
PathIshOrConn = PathIsh | Connection


def expand_path(path: PathIsh) -> Path:
    if isinstance(path, str):
        path = Path(path)
    return path.expanduser().absolute()


# keep as RuntimeError for backwards compatibility
class BrowserexportError(RuntimeError):
    pass
