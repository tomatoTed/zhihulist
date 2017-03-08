from zhihulist import Zhihu
z = Zhihu()
# z.auth(cookie="your_cookie_str")
# z.auth(username='your_phone_or_email',password='your_password')
z.auth()
z.me()
z.follower()