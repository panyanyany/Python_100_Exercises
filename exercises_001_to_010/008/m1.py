items = input('输入二进制:').split(',')

array = []
for p in items:
    i = int(p, 2)
    if not i % 5:
        array.append(p)

print(','.join(array))
