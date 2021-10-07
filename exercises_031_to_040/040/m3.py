tu = (1, 2)
li = [1, 2]

print('tu', id(tu))
print('li', id(li))

tu += (3,)  # (1, 2, 3)
li += [3]  # [1, 2, 3]

print()
print('tu', id(tu))  # id 会变
print('li', id(li))  # id 不变
