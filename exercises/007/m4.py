import json

a = [1, 2, 3]
t = json.dumps(a)
# print(t)
b = json.loads(t)
print(id(a) == id(b), id(a), id(b))
print(b)
