def Main(operation: str, args: tuple) -> int:
    a = TestAdd(1, 2)
    return a


def TestAdd(a: int, b: int) -> int:
    return a + b
