import requests
from excelDo import read_data
import csv
# def m_request(method,url,data):
#     if method == 'get':
#         response = requests.get(url,data)
#     else:
#         response = requests.post(url,data)
#     return response
class readWrite():
    rows = [
            [1,'xiaoming','male',168,23],
            [1,'xiaohong','female',162,22],
            [2,'xiaozhang','female',163,21],
            [2,'xiaoli','male',158,21]
        ]
    rows_dict = [
        {
            'host': '123.57.53.215',
            'port': 3306,
            'user': 'root',
            'password': 'qingclass@2020',
            'db': 'mysb_test',
            'charset': 'utf8mb4',
        }
        ]
    header = ['host','port','user','password','db','charset']

    # row = csv.DictWriter(open('config.csv','w'),header)
    # row.writeheader()
    # row.writerows(rows_dict)
    # open('config.csv','w').close()
    def read(self,path):
        reader = csv.DictReader(open(path,'r'))
        list = []
        for i in reader:
            list.append(i)
        open(path,'r').close()
        return list
if __name__ == '__main__':
    base = readWrite()
    path = 'config.csv'
    f = base.read(path=path)
    print(f)