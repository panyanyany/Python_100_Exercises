def mysum(*args):
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    total = 0
    for item in args:
        if isinstance(item, (int, float)):
            total += item
        else:
            total += float(item)
    return total


print(mysum([1, 2, '3.4']))
print(mysum(1, 2, '3.4'))
