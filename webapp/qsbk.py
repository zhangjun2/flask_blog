import urllib
import urllib.request
import urllib.response
from functools import reduce

page = 1
# url ='http://www.qiushibaike.com'
url = 'https://www.qiushibaike.com/8hr/page/2'

class qsbk:

    def __init__(self):
        self.url = 'http://www.qiushibaike.com'
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}

    def post_req(self, url):

        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            print(content)

        except (urllib.request.URLError) as e:
            print(e)


# qsbk = qsbk()
# qsbk.post_req(url)

# def prod(L):
#     return reduce(lambda x,y:x*y,L)
#
# print(prod([1,2,3,5,6]))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[1]

L2 = sorted(L, key=by_name,reverse=True)
print(L2)