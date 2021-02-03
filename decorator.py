import datetime
import time
import functools
def monitor(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start_time = int(time.time() * 1000)
        func(*args, **kw)
        end_time = int(time.time() * 1000)
        print('响应时间：%d' % (end_time-start_time))
    return wrapper

# class abc():
#     def __init__(self, func):
#         self.func = func
#     def inner(self):
#         start_time = int(time.time() * 1000)
#         self.func()
#         end_time = int(time.time() * 1000)
#         print('响应时间：%d' % (end_time-start_time))
# @abc
# def login():
#     base_url = 'https://api-test-admin-zuul.qkduo.cn/'
#     login_path = 'auth-center/nologin/login'
#     # getUserInfo_path = 'auth-center/noauth/getUserInfo'
#     login_data = {
#         'email': 'admin@qingclass.com',
#         'password': 'e10adc3949ba59abbe56e057f20f883e'
#     }
#     response = requests.post(url=base_url + login_path, data=login_data)
# login()