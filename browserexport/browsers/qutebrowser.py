from urllib.parse import unquote

from .common import (
    handle_path,
    datetime,
    timezone,
    handle_glob,
    Path,
    Paths,
    Metadata,
    PathIshOrConn,
    Visit,
    Schema,
    execute_query,
    Iterator,
    Browser,
)


class Qutebrowser(Browser):
    detector = "CompletionMetaInfo"
    schema = Schema(
        cols=[
            "H.url",
            "H.title",
            "H.atime",
        ],
        where="FROM History as H",
        order_by="H.atime",
    )

    @classmethod
    def extract_visits(cls, path: PathIshOrConn) -> Iterator[Visit]:
        for row in execute_query(path, cls.schema.query):
            yield Visit(
                url=unquote(row["url"]),
                dt=datetime.fromtimestamp(row["atime"], timezone.utc),
                metadata=Metadata.make(title=row["title"]),
            )

    @classmethod
    def data_directories(cls) -> Paths:
        return handle_path(
            {
                "linux": "~/.local/share/qutebrowser",
                "darwin": "~/Library/Application Support/qutebrowser/",
                # I'm not sure, does this work...?
                # "win32": windows_appdata_paths(r"qutebrowser\User Data"),
            },
            browser_name=cls.__name__,
        )

    @classmethod
    def locate_database(cls, profile: str = "*") -> Path:
        dd = cls.data_directories()
        return handle_glob(dd, "history.sqlite")
