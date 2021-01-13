from __future__ import annotations

from typing import Any, Collection

from boa3.builtin.interop.enumerator import Enumerator


class Iterator:
    def __init__(self, entry: Collection):
        pass

    @property
    def key(self) -> Any:
        return None

    @property
    def value(self) -> Any:
        return None

    def next(self) -> bool:
        pass

    def concat(self, other: Iterator) -> Iterator:
        pass

    def keys(self) -> Enumerator:
        pass

    def values(self) -> Enumerator:
        pass
