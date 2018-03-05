# encoding: utf-8
'''
模拟Github登陆步骤：
    1、请求头:self.headers,请求url
    2、设置session,保存登陆信息cookies,生成github_cookie文件
    3、POST表单提交,请求数据格式post_data
    4、authenticity_token获取
    5、在个人中心验证判断是否登陆成功,输出个人中心信息即登陆成功

'''

import requests
import re
from lxml import etree

try:
    import cookielib
except:
    import http.cookiejar as cookielib


class GithubLogin():
    def __init__(self):
        # url
        self.loginUrl = 'http://mxy.chinamobo.com/admin.php/login'
        self.postUrl = 'http://mxy.chinamobo.com/admin.php/login'
        self.select = 'http://mxy.chinamobo.com/admin.php/login/select?eid=886&type=&referrer=&backurl='
        self.profileUrl = 'http://mxy.chinamobo.com/admin.php/train/train/index'

        # 设置请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        }

        # 设置session
        self.session = requests.session()
        # 生成github_cookie文件
        self.session.cookies = cookielib.LWPCookieJar(filename='mobo_cookie')

    def post_account(self, email, password):
        post_data = {
            'LoginForm[username]': email,
            'LoginForm[password]': password,
            'LoginForm[username1]': '',
            'LoginForm[passwordw]': '',
            'LoginForm[rememberMe]': 1,
            'YII_CSRF_TOKEN': self.get_token(),
            'auth_code': ' ',
        }
        response = self.session.post(self.postUrl, data=post_data, headers=self.headers)
        # 保存cookiesz
        self.session.cookies.save()

    def load_cookie(self):
        try:
            self.session.cookies.load(ignore_discard=True)
        except:
            print('cookie 获取不成功')

    # 获取authenticity_token
    def get_token(self):
        response = self.session.get(self.loginUrl, headers=self.headers)
        print response.text;
        matchObj = re.search(r'YII_CSRF_TOKEN\':\'(.*)\', \'auth_code', response.text, re.M | re.I)
        return matchObj.group(1);
    # 判断是否登陆成功
    def checkLogin(self):

        self.load_cookie()
        self.session.get(self.select, headers=self.headers)
        response = self.session.get(self.profileUrl, headers=self.headers)
        f = open("out.html", "w")
        f.write( response.text.encode('utf-8', 'ignore'))


if __name__ == "__main__":
    github = GithubLogin()
    # 输入自己email账号和密码
    github.post_account(email='*********', password='e10adc3949ba59abbe56e057f20f883e')
    # 验证是否登陆成功
    #github.checkLogin();
