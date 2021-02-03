import requests
import json
class BaseRequest():
    def request_get(self,session,url, data, header):
        res = session.get(url=url, params=data, headers=header)
        return res
    def request_post(self,session,url, data, header):
        res = session.post(url=url, data=data, headers=header)
        return res
    def run_main(self,session,method,url, data=None, header=None):
        try:
            res = ''
            if method == 'get':
                res = BaseRequest().request_get(session=session,url=url,data=data,header=header)
            elif method == 'post':
                res = BaseRequest().request_post(session=session,url=url, data=data, header=header)
            return res
        except Exception as e:
            print('请求主函数调用失败：{}'.format(e))
    def get_token(self,r):
        a = json.loads(r.text)
        token = a.get('data').get('token')
        return token
        header = {'cookie': 'zuulToken=' + token}
if __name__ == '__main__':
    session = requests.session()
    base_request = BaseRequest()
    base_url = 'https://api-test-admin-zuul.qkduo.cn/'
    login_path = 'auth-center/nologin/login'
    getUserInfo_path = 'auth-center/noauth/getUserInfo'
    login_data = {
        'email': 'admin@qingclass.com',
        'password': 'e10adc3949ba59abbe56e057f20f883e'
    }
    getUserInfo_data = {}
    login_send = base_request.run_main(session=session,method='post',url=base_url+login_path, data=login_data)
    token = BaseRequest().get_token(login_send)
    header = {'cookie': 'zuulToken=' + token}
    getUserInfo_send = base_request.run_main(session=session,method='get',url=base_url + getUserInfo_path, data=getUserInfo_data,header=header)
    print(login_send.text)
    print(getUserInfo_send.text)
