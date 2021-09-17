# Mac系统下会报错，因为 windows 的默认编码是 gbk，mac 是 utf8
with open('./storage/windows默认中文.txt', 'r') as fp:
    print(fp.read())
