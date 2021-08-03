line = input('输入用户名：')


def is_valid(name: str):
    flags = []
    for c in name:
        if c.islower() or c.isnumeric() or c == '_':
            flags.append(1)
        else:
            flags.append(0)

    if not all(flags):
        return False

    if 6 <= len(name) <= 12:
        return True
    return False


print(is_valid(line))
