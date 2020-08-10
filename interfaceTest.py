import requests
from excelDo import read_data
base_url = 'https://test-msyb-cms-api.qingclasswelearn.com'
payload = {'loginName':'admin','password':'qingclass'}
s = requests.session()
r = s.post(base_url+'/admin/sign-in',data=payload)
print(r.text)
print('hdhdjh')
