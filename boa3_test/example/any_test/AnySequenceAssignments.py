from typing import Any, Sequence


def Main():
    any_list = [True, 1, 'ok']
    int_list = [1, 2, 3]
    any_tuple = (True, 1, 'ok')
    bool_tuple = True, False

    a: Sequence[Any]
    a = any_list
    a = any_tuple
    a = 'some_string'
    a = int_list
    a = bool_tuple
