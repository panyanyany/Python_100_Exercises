# 错误写法
a = [1, 2, 3]
b = a
print(id(a) == id(b), id(a), id(b))
print(b)

b.pop()

print(b)
print(a)
