data = input('输入二进制:').split(',')
array = filter(lambda i: int(i, 2) % 5 == 0, data)
array = list(array)
print(",".join(array))
