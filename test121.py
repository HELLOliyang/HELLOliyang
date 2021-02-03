import requests
import time
import json
t = time.time()
time_now = int(round(t * 1000))
url = 'http://testapi.qkduo.cn/dev-bwm6/login/web/loginByPhone'
data = {'phone':'1853669666',
        'code':'2364',
        't':time_now}
session = requests.session()
res = session.post(url=url, data=data)
print(res.text)
a = json.loads(res.text)
token = a.get('data').get('token')
print(token)
header = {'Cookie': 'pToken=' + token}
url2 = 'http://testapi.qkduo.cn/dev-bwm6/buyMessage/liveReadyBuySendMessage'
time_now2 = int(round(t * 1000))
data2 = {'liveId':'ll_909725907',
        't':time_now2}
res = session.get(url=url2, params=data2, headers=header)
print(res.text)