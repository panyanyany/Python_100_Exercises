data = input('输入二进制：').split(',')


def check(x):
    return int(x, 2) % 5 == 0


array = filter(check, data)
array = list(array)
print(",".join(array))
