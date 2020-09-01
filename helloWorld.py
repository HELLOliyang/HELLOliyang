import requests
from excelDo import read_data
def m_request(method,url,data):
    if method == 'get':
        response = requests.get(url,data)
    else:
        response = requests.post(url,data)
    return response