with open('./storage/windows默认中文.txt', 'r', encoding='gbk') as fp:
    print(fp.read())

print('=========')

with open('./storage/utf8中文.txt', 'r', encoding='utf8') as fp:
    print(fp.read())

print('=========')

with open('./storage/utf8中文.txt', 'r') as fp:
    print(fp.read())
