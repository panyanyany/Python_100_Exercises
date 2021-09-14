import requests
import json

response = requests.get('http://httpbin.org/ip')
jd = json.loads(response.text)
print('我的IP是：', jd['origin'])
