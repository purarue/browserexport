from .common import (
    handle_path,
    handle_glob,
    Path,
    Paths,
    # windows_appdata_paths,
)


from .chrome import Chrome


class Qutebrowser(Chrome):
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
