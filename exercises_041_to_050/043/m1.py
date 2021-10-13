li = ['a', 'b', 'c']
# remove 传入元素本身
print(li.remove('b'), li)

li = ['a', 'b', 'c']
# pop 传入下标, 返回被删除元素
print(li.pop(1), li)

# remove 相当于这个样子：
li = ['a', 'b', 'c']
b_index = li.index('b')
li.pop(b_index)
print(li)

li = ['a', 'b', 'c']
# del 也是传入下标
del li[1]
print(li)

li = ['a', 'b', 'c']
# 但 del 可以删除一个范围内的所有元素
del li[0:2]
print(li)

li = ['a', 'b', 'c']
# del 还可以删除变量
del li
# 会报错，因为 li 不存在了
print(li)
