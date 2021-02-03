import pymysql
import requests
import time
import json
import re
from fileIO import csvIO
class DB():
    def DML(self,sql):
        connection = pymysql.connectconn = pymysql.connect(host='172.17.227.221', port=3306, user='root', passwd='iytAQbjN#GSKhe21', db='qkd_passport', charset='utf8')

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                connection.commit()
                cursor.close()
        finally:
            connection.close()
        return result
if __name__ =='__main__':
    base = DB()
    sql = 'SELECT phone from t_user where phone is not null and id>33518777 and id <33518923'
    sql2 = 'SELECT count(*) from t_user where phone is not null and id>33518775 and id <33518923'
    c = base.DML(sql=sql)
    Messgecount = base.DML(sql=sql2)
    print(Messgecount[0][0])
    for i in range(60):
        d = c[i][0]
        print(d)
        t = time.time()
        time_now = int(round(t * 1000))
        # url = 'http://testapi.qkduo.cn/dev-bwm6/login/web/loginByPhone'
        url = 'http://test.api.qkduo.cn/login/web/loginByPhone'
        data = {'phone': d,
                'code': '2364',
                't': time_now}
        session = requests.session()
        res = session.post(url=url, data=data)
        print(res.text)
        a = json.loads(res.text)
        token = a.get('data').get('token')
        print(token)
        header = {'Cookie': 'pToken=' + token}
        # url2 = 'http://testapi.qkduo.cn/dev-bwm6/buyMessage/liveReadyBuySendMessage'
        url2 = 'http://test.api.qkduo.cn/buyMessage/liveReadyBuySendMessage'
        time_now2 = int(round(t * 1000))
        cc_liveid = 'll_909725907'
        huantuo_liveid = 'll_f90bcd82a'
        data2 = {'liveId': cc_liveid,
                 't': time_now2}
        res = session.get(url=url2, params=data2, headers=header)
        print(res.text)
        time.sleep(1)