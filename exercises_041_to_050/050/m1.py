import json

jd = {
    'a': 1,
    'b': [3, 2, ]
}

filename = 't.json'
# 这一步也叫序列化
with open(filename, 'w+') as fp:
    json.dump(jd, fp)

# 这一步也叫反序列化
with open(filename, 'r') as fp:
    jd2 = json.load(fp)

print(jd2)
