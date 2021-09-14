import requests

response = requests.get('http://httpbin.org/ip')
print('我的IP是：', response.text)
