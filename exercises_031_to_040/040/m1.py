tu = (1, 2)
li = [1, 2]

try:
    # tuple 不可变，所以不能赋值，会出错
    tu[0] = 3
    print('tu', tu)
except Exception as e:
    print(e)

li[0] = 3
print('li', li)
