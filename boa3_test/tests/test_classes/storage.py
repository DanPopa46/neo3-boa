from typing import Any, Dict, List, Union

from boa3.neo.utils import contract_parameter_to_json, stack_item_from_json
from boa3.neo.vm.type.Integer import Integer


class Storage:
    def __init__(self):
        self._dict: Dict[StorageKey, StorageItem] = {}

    def pop(self, key: bytes):
        storage_key = StorageKey(key)
        return self._dict.pop(storage_key)

    def clear(self):
        return self._dict.clear()

    def copy(self):
        storage = Storage()
        storage._dict = self._dict.copy()
        return storage

    def to_json(self) -> List[Dict[str, Any]]:
        return [{'key': key.to_json(),
                 'value': item.to_json()
                 } for key, item in self._dict.items()
                ]

    @classmethod
    def from_json(cls, json: Union[Dict[str, Any], List[Dict[str, Any]]]):
        if not isinstance(json, list):
            json = [json]

        new_storage = {}
        for storage_value in json:
            key = StorageKey.from_json(storage_value['key'])
            value = StorageItem.from_json(storage_value['value'])
            new_storage[key] = value

        storage = Storage()
        storage._dict = new_storage
        return storage

    def add_token(self, token_script: bytes, script_hash: bytes, amount: int) -> bool:
        if len(token_script) != 20 or len(script_hash) != 20 or amount <= 0:
            return False

        from boa3_test.tests.test_classes.nativetokenprefix import get_native_token_data
        token_prefix, token_id = get_native_token_data(token_script)
        if token_prefix is None or token_id is None:
            return False

        balance_key = token_prefix + script_hash
        if balance_key in self._dict:
            balance = Integer.from_bytes(self[balance_key])
        else:
            balance = 0

        balance += amount

        from boa3_test.tests.test_classes.nativeaccountstate import NativeAccountState
        key = StorageKey(balance_key)
        key._ID = token_id
        self._dict[key] = StorageItem(NativeAccountState(balance).serialize())
        return True

    def __contains__(self, item: bytes) -> bool:
        return StorageKey(item) in self._dict

    def __getitem__(self, item: bytes) -> Any:
        storage_key = StorageKey(item)
        return self._dict[storage_key].value

    def __setitem__(self, key: bytes, value: Any):
        from boa3.neo.vm.type import StackItem
        storage_key = StorageKey(key)
        self._dict[storage_key] = StorageItem(StackItem.serialize(value))


class StorageKey:
    def __init__(self, key: bytes):
        self._ID = 0
        self._key: bytes = key

    def to_json(self) -> Dict[str, Any]:
        return {'id': self._ID,
                'key': contract_parameter_to_json(self._key)
                }

    @classmethod
    def from_json(cls, json: Dict[str, Any]):
        k = stack_item_from_json(json['key'])
        if isinstance(k, str):
            from boa3.neo.vm.type.String import String
            k = String(k).to_bytes()

        key = StorageKey(k)
        key._ID = json['id']
        return key

    def __eq__(self, other) -> bool:
        return isinstance(other, StorageKey) and self._key == other._key

    def __str__(self) -> str:
        return self._key.__str__()

    def __hash__(self):
        return self._key.__hash__()


class StorageItem:
    def __init__(self, value: bytes, is_constant: bool = False):
        self._is_constant: bool = is_constant
        self._value: bytes = value

    @property
    def value(self) -> bytes:
        return self._value

    def to_json(self) -> Dict[str, Any]:
        return {'isconstant': self._is_constant,
                'value': contract_parameter_to_json(self._value)
                }

    @classmethod
    def from_json(cls, json: Dict[str, Any]):
        value = stack_item_from_json(json['value'])
        if isinstance(value, str):
            from boa3.neo.vm.type.String import String
            value = String(value).to_bytes()

        item = StorageItem(value, json['isconstant'])
        return item

    def __str__(self) -> str:
        return self._value.__str__()
