names_input = input('输入姓名：')
names = names_input.split('，')
candies_input = input('输入分数：')
candies = candies_input.split('，')

candies += [0] * (len(names) - len(candies))

stat = {}
for i, name in enumerate(names):
    stat[name] = candies[i]

while True:
    query = input('输入要查询的名字：')
    if query in stat:
        print(stat[query])
    else:
        print('名字不存在！')
