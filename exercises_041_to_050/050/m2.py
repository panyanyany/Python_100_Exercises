import pickle

jd = {
    'a': 1,
    'b': [3, 2, ]
}
filename = 't.bin'
# 注意打开模式有个 'b' 即二进制模式
with open(filename, 'w+b') as fp:
    pickle.dump(jd, fp)

with open(filename, 'rb') as fp:
    jd2 = pickle.load(fp)
print(jd2)
