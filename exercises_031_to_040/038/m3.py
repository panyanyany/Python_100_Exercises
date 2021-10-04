def can_iter(v):
    try:
        for i in v:
            pass
        return True
    except:
        return False


print(can_iter(range(10)))
print(can_iter([1, 2]))
print(can_iter({'a': 1}))
print(can_iter('hello'))
print(can_iter(1))
