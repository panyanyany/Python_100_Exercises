# 同一行内输入
line = input('输入3个数（空格分隔）:')
l = line.split(' ')
for i, item in enumerate(l):
    l[i] = int(item)
l.sort()
print(l)
