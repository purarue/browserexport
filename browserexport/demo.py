from collections import Counter
from pprint import pprint

from urllib.parse import urlsplit

from .model import Visit


def demo_visit(visits: list[Visit]) -> None:
    print("Demo: Your most common sites....")
    pprint(Counter(map(lambda v: urlsplit(v.url).netloc, visits)).most_common(10))
