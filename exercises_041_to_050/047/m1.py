stat = {'a': 1}

print(stat['a'])

# 直接拿 b 会出错
# print(stat['b'])

# 通过 get 拿不会出错
print(stat.get('b'))
