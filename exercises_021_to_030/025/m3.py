import requests

response = requests.get('http://httpbin.org/ip')
jd = response.json()
print('我的IP是：', jd['origin'])
