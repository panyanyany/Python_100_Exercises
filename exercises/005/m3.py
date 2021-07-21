# 逆序
line = input('输入3个数:')
l = line.split(' ')
for i, item in enumerate(l):
    l[i] = int(item)
l.sort(reverse=True)
# l.sort(key=lambda e: -1 * e)
print(l)
