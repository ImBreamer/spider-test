import urllib.request
from urllib import request, error, parse
from http import cookiejar
from bs4 import BeautifulSoup

class BeautifulSoupVideoMain(object):

    def __init__(self):
        pass

if __name__ == "__main__":
    linkUrl = "https://www.imooc.com/learn/790";

    def get_video_links():
        response = urllib.request.urlopen(linkUrl)
        soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')
        return [a.attrs.get('href') for a in soup.select('a.J-media-item')]

    def cookie_save_test():
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookiejar.MozillaCookieJar(filename)
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handler = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(handler)
        # 此处的open方法打开网页
        response = opener.open('http://www.baidu.com')
        # 保存cookie到文件
        cookie.save(ignore_discard=True, ignore_expires=True)

    def cookie_load_test():
        # 设置保存cookie的文件的文件名,相对路径,也就是同级目录下
        filename = 'cookie.txt'
        # 创建MozillaCookieJar实例对象
        cookie = cookiejar.MozillaCookieJar()
        # 从文件中读取cookie内容到变量
        cookie.load(filename, ignore_discard=True, ignore_expires=True)
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handler = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(handler)
        # 此用opener的open方法打开网页
        response = opener.open('http://www.baidu.com')
        # 打印信息
        print(response.read().decode('utf-8'))

    def cookie_test():
        # 声明一个CookieJar对象实例来保存cookie
        cookie = cookiejar.CookieJar()
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handler = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(handler)
        # 此处的open方法打开网页
        response = opener.open('http://www.baidu.com')
        # 打印cookie信息
        for item in cookie:
            print('Name = %s' % item.name)
            print('Value = %s' % item.value)

    def login_do():
        # 登陆地址
        login_url = 'https://m.imooc.com/passport/user/login'
        # User-Agent信息
        user_agent = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko)' \
                     ' Chrome/66.0.3359.139 Mobile Safari/537.36'
        # Headers信息
        head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
        # 登陆Form_Data信息
        Login_Data = {}
        Login_Data['password'] = 'beyond1983ju'
        Login_Data['referer'] = 'https://m.imooc.com'
        Login_Data['username'] = '15032232392'
        Login_Data['verify'] = ''
        # 使用urlencode方法转换标准格式
        logingpostdata = parse.urlencode(Login_Data).encode()
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookiejar.MozillaCookieJar(filename)
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        cookie_support = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(cookie_support)
        # 创建Request对象
        req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

        # 面向对象地址
        date_url = 'https://m.imooc.com/video/13928'
        # 面向对象
        # Date_Data = {}
        # Date_Data['action'] = 'get_date_contact'
        # Date_Data['postId'] = '4128'
        # 使用urlencode方法转换标准格式
        # datepostdata = parse.urlencode(Date_Data).encode('utf-8')
        req2 = request.Request(url=date_url, headers=head)
        try:
            # 使用自己创建的opener的open方法
            response1 = opener.open(req1)
            # 保存cookie到文件
            cookie.save(ignore_discard=True, ignore_expires=True)
            response2 = opener.open(req2)
            html = response2.read().decode('utf-8')
            index = html.select('video.vjs-tech')
            # 打印查询结果
            print('联系邮箱:%s' % index.attrs.get('src'))

        except error.URLError as e:
            if hasattr(e, 'code'):
                print("HTTPError:%d" % e.code)
            elif hasattr(e, 'reason'):
                print("URLError:%s" % e.reason)

    def login_url_test():
        # 登陆地址
        login_url = 'https://www.imooc.com/user/ssologin?token=8df_sm8-TJkdvzQr5HKnBw9CcCivrLnmY4P8_ea4Po8fCJwwP5Q5HCZ7OIhrDlIy4s43wn36wvmu-bF60prKur04AOx65xuOrg64A1hYoOo1E-hnS7I7Ra9BKk6AxrGyuKKAAfrqWV7LiDqiiHqaSI7m0Q2L7NkYVfzRy9ixtyLAOB2cX0HPdIaW3u3mNKlqif1ymLcB5wTTjEOODKyd78ONqwG9a-7YmSBOj_FsN0a6xpQnHhORsWGCimJXDFAg-7y5X30VKvmGWPHJf&callback=jQuery19109798422707792591_1526366840970&_=1526366840973'
        # User-Agent信息
        user_agent = r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                     r' Chrome/66.0.3359.139 Safari/537.36'
        # Headers信息
        head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
        # 登陆Form_Data信息
        Login_Data = {}
        Login_Data['password'] = 'ziSgvJ8HA4+kephP7UG8xDmrk6eYW+31P491IVM+TUEJgjYHHzYXwCZBzASmz+MTBOMDao6as+nhgPs+1HZAyubKCz7Vfd5hq00+Z0VNteukKugO5rngAZ4a0jKlDBaN+tWT8DgmUSg+97ksN1Mx1YbksF91BH/cg+PEOk+00pE='
        Login_Data['referer'] = 'https://m.imooc.com'
        Login_Data['username'] = '15032232392'
        Login_Data['browser_key'] = 'd7c4003f42a29cb4b9f134e50288fa55'
        Login_Data['remember'] = '1'
        Login_Data['pwencode'] = '1'
        Login_Data['verify'] = ''
        # 使用urlencode方法转换标准格式
        logingpostdata = parse.urlencode(Login_Data).encode()
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie_login.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookiejar.MozillaCookieJar(filename)
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        cookie_support = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(cookie_support)
        # 创建Request对象
        req1 = request.Request(url=login_url, data=logingpostdata, headers=head)
        # 使用自己创建的opener的open方法
        response1 = opener.open(req1)
        # 保存cookie到文件
        cookie.save(ignore_discard=True, ignore_expires=True)

    # print(login_url_test())
    print(cookie_save_test())
