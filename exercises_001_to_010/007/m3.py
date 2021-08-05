# 利用类构造来复制
a = [1, 2, 3]
b = list(a)
print(id(a) == id(b), id(a), id(b))
print(b)
