from datetime import timedelta
import datetime
import requests
class interfaceTest():
    def __int__(self):
        self.session = requests.session()
        self.base_url = 'https://api-test-admin-zuul.qkduo.cn/'
        self.login_path = 'auth-center/nologin/login'
        getUserInfo_path = 'auth-center/noauth/getUserInfo'
        self.login_data = {
            'email': 'admin@qingclass.com',
            'password': 'e10adc3949ba59abbe56e057f20f883e'
        }
    def login(self):
        requests = self.session.post(url=self.base_url+self.login_path,data=self.login_data)
        return requests.text
    # def get_today(self):
    #     now_time = datetime.datetime.now()
    #     today = now_time.strftime('%Y-%m-%d %H:%M:%S')
    #     return today
    # def get_onedaytime(self,day):
    #     now_time = datetime.datetime.now()
    #     day_time = now_time+timedelta(days=day)
    #     oneday = day_time.strftime('%Y-%m-%d %H:%M:%S')
    #     return oneday
if "__main__" == __name__:
    day = 7
    a = interfaceTest().get_onedaytime(day=day)
    b = interfaceTest().get_today()
    print('今天后的日期：'+b)
    print(str(day)+'天后的日期：'+a)