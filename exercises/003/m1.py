names_input = input('输入姓名：')  # 小明 小红 小青
names = names_input.split(' ')
scores_input = input('输入分数：')  # 3 2
scores = scores_input.split(' ')

stat = {}
for i, name in enumerate(names):
    if i < len(scores):  # 避免 scores 访问越界
        stat[name] = scores[i]
    else:
        stat[name] = 0

while True:
    query = input('输入要查询的名字：')
    if query in stat:
        print(stat[query])
    else:
        print('名字不存在！')
