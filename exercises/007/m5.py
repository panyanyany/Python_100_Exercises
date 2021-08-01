# 直接复制元素
a = [1, 2, 3]
b = []
for e in a:
    b.append(e)
print(id(a) == id(b), id(a), id(b))
print(b)
