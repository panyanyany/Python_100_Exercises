# 利用 json 序列化/反序列化 来复制
import json

a = [1, 2, 3]
t = json.dumps(a)
# print(t)
b = json.loads(t)
print(id(a) == id(b), id(a), id(b))
print(b)
