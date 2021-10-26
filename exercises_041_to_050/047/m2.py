stat = {}
colors = ['红', '蓝', '红']
for color in colors:
    # 旧的写法：
    if color not in stat:
        stat[color] = 0
    stat[color] += 1

print(stat)

stat = {}
colors = ['红', '蓝', '红']
for color in colors:
    # 新的写法：
    # get 既避免了 key 不存在导致的错误，又可以提供默认值
    stat[color] = stat.get(color, 0) + 1

print(stat)
