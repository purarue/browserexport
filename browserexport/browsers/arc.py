from .common import (
    handle_path,
    Paths,
)

from .chromium import Chromium


class Arc(Chromium):
    """https://arc.net/"""

    @classmethod
    def data_directories(cls) -> Paths:
        return handle_path(
            {
                # macOS only browser, so no linux/darwin distinction
                "darwin": "~/Library/Application Support/Arc/User Data/",
            },
            browser_name=cls.__name__,
        )
