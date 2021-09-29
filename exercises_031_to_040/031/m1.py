import pandas

scores = pandas.read_excel('./storage/成绩单.xlsx')
print('------ 当前表格：')
print(scores)

print('------ 开始筛选重复数据：')

# 新建个 DataFrame 用来保存过滤后的数据
new_scores = pandas.DataFrame()
# 用来标记是否已存在
existed_name = {}
for index, row in scores.iterrows():
    if row['姓名'] in existed_name:
        print('发现重复项：', row['姓名'], row['成绩'])
        continue
    existed_name[row['姓名']] = True
    new_scores = new_scores.append(row, ignore_index=True)

print('------ 筛选后的表格：')
print(new_scores)

print('------ 正在保存到新表格中')
new_scores.to_excel('./storage/成绩单-02.xlsx', index=False)
print('------ 完成！')
