import threading
import requests
import time
import psutil
from decorator import monitor
class performanceTesting():
    def __init__(self):
        self.session = requests.session()
    # @monitor
    def login(self):
        base_url = 'https://api-test-admin-zuul.qkduo.cn/'
        login_path = 'auth-center/nologin/login'
        # getUserInfo_path = 'auth-center/noauth/getUserInfo'
        login_data = {
            'email': 'admin@qingclass.com',
            'password': 'e10adc3949ba59abbe56e057f20f883e'
        }
        response = self.session.post(url=base_url + login_path, data=login_data)
        print(response.text)
    def control(self):
        self.login()
        self.activity_monitor()
        time.sleep(3)
    def activity_monitor(self):
        cpu_monitor = psutil.cpu_percent()
        memory_monitor = psutil.swap_memory()
        print('cpu占用率: %.2f%% ' % (cpu_monitor))
        print(memory_monitor)
        print('内存占用率: %.2f%% ' %sorted(memory_monitor)[0])
if __name__ == '__main__':
    print('***********主线程开始**********')
    base = performanceTesting()
    # for i in range(1):
    #     a = threading.Thread(target=base.control())
    #     a.start()
    #     a.join()
    base.login()
    print('**********主线程结束************')