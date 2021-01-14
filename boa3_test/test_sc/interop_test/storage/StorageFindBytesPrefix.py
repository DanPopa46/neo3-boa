from typing import Union

from boa3.builtin import public
from boa3.builtin.interop.enumerator import Enumerator
from boa3.builtin.interop.storage import find, put


@public
def find_by_prefix(prefix: bytes) -> Enumerator:
    return find(prefix)


@public
def put_on_storage(key: Union[str, bytes], value: Union[int, str, bytes]):
    put(key, value)
