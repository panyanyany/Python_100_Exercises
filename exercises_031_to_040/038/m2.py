from collections.abc import Iterable


def can_iter(v):
    return isinstance(v, Iterable)


print(can_iter(range(10)))
print(can_iter([1, 2]))
print(can_iter({'a': 1}))
print(can_iter('hello'))
print(can_iter(1))
