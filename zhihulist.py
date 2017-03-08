from pyquery import PyQuery as pq
import requests as req
import util
import re
import pickle
import os


class Zhihu:

    __DOMAIN = 'https://www.zhihu.com'
    __HEADER={
                "Accept": "text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, * / *;q = 0.8",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
                "Accept - Language": "zh - CN, zh;q = 0.8, en;q = 0.6",
                'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
            }
    __CACHE_NAME="cache"
    __session = None
    __cookie = None

    __info=None
    __username=None
    __password=None

    def __init__(self):
        self.__session = req.session()
        self.__session.headers.update(self.__HEADER)

    # 登录
    def auth(self, cookie=None, username=None, password=None,cache=True):
        if cookie is not None and type(cookie) == str:
            self.__cookie = util.cookie2dic(cookie)
            self.__session.cookies.update(self.__cookie)
            if cache:
                self.__save_cookie()
        if username is not None and password is not None:
            r1=self.__get(self.__DOMAIN)
            d = pq(r1.text)
            xsrf = d("input[name=_xsrf]").val()

            kw=None
            if util.is_email(username):
                kw = "email"
            if util.is_phone(username):
                kw = "phone_num"
            data={kw: username, "password": password, "captcha_type": "cn","_xsrf":xsrf}
            r = self.__post("/login/" + kw, data)
            self.__cookie = r.cookies
            if cache:
                self.__save_cookie()
            return True
        if os.path.exists(self.__CACHE_NAME):
            self.__cookie =self.__get_cookie()
            self.__session.cookies.update(self.__cookie)

    # 个人资料
    def me(self):
        r = self.__get(self.__DOMAIN)
        if r.status_code == 200:
            d = pq(r.text)
            img=d("img.Avatar")
            self.__info={
                "name":img.attr("alt"),
                "link": d("a.zu-top-nav-userinfo").attr("href"),
                "avatar":img.attr("src"),
            }
            self.__info['url_token']=self.__info['link'].split("/")[-1]
            print(self.__info)
        else:
            print(self.__info)

    # 查看粉丝列表
    def follower(self, url_token=None, offset=0, limit=20):
        url="/api/v4/members/{0}/followers"
        if url_token is None and self.__info['url_token'] is not None:
            url_token=self.__info['url_token']
        url=url.format(url_token)
        params={
            "include":"data[*].answer_count, articles_count, gender, follower_count, is_followed, is_following, badge[?(type = best_answerer)].topics",
            "offset":offset,
            "limit":limit
        }
        r=self.__get(url,params)
        json=r.json()
        tpl="{0}:  昵称:{name}, 性别:{1}, 说明:{headline}, 回答数:{answer_count}, 文章数:{articles_count}, 关注者:{follower_count}, 标识:{url_token}, 头像:{avatar_url}"
        if(json is not None):
            #print(json['paging'])
            for i,item  in enumerate(json['data']):
                print(tpl.format(i,util.get_gender_name(item['gender']),**item))

    def __get(self, url,params=None):
        if re.match(r"https?://",url) is None:
            url=self.__DOMAIN+url
        r = self.__session.get(url,params=params)
        if r.status_code!=200:
            d={"error":">"*15,"state":r.status_code,"msg":r.text}
            print(d)
        return r

    def __post(self, url, data=None):
        if re.match(r"https?://", url) is None:
            url = self.__DOMAIN+url
        r = self.__session.post(url, data,verify=False)
        if r.status_code != 200:
            d = {"error": ">"*15, "state": r.status_code, "msg": r.text}
            print(d)
        return r

    # 缓存cookie到文件
    def __save_cookie(self):
        with open(self.__CACHE_NAME, mode='wb') as f:
            pickle.dump(self.__cookie, f)

    # 从文件读取cookie
    def __get_cookie(self):
        with open(self.__CACHE_NAME, mode='rb') as f:
            r=pickle.load(f)
            return r



