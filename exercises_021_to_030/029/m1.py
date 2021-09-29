import requests

# 模拟表单提交，不能传太复杂的对象
response = requests.post('http://httpbin.org/post', data={
    'hello': 'world',
    'dict': {'a': 1},
    'list': [1, 2, 3],
})
print(response.text)

print("----分隔线----")

# 模拟 ajax 提交, 可以传复杂对象
response = requests.post('http://httpbin.org/post', json={
    'hello': 'world',
    'dict': {'a': 1},
    'list': [1, 2, 3],
})
print(response.text)
