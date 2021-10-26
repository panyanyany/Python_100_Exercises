import pickle

jd = {
    'a': 1,
    'b': [3, 2, ]
}
filename = 't.bin'


# 也可以保存 python 对象，比如函数：

def greet():
    print('hello world')


with open(filename, 'w+b') as fp:
    pickle.dump(greet, fp)

with open(filename, 'rb') as fp:
    greet2 = pickle.load(fp)

greet2()
