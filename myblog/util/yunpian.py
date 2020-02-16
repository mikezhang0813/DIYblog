from urllib import request
from urllib.parse import  urlencode
from myblog.settings import *
import random
def send_sms(code,mobile):
        """
        通用接口发短信
        """
        text='【gouzidui】您的验证码是{}'.format(code)
        data = urlencode({'apikey': YUN_PIAN_API_KEY, 'text': text, 'mobile':mobile}).encode()
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }

        req = request.Request(url=YUN_PIAN_SMS_SEND_URI,headers=headers,data=data)
        res = request.urlopen(req,timeout=30).read().decode()
        return res


def generate_number():

    ''' 随机生成6位的验证码 '''
    code_list = []
    for i in range(4):
        random_num = random.randint(0, 9) # 随机生成0-9的数字
        # 利用random.randint()函数生成一个随机整数a，使得65<=a<=90
        # 对应从“A”到“Z”的ASCII码


        code_list.append(str(random_num))

    verification_code = ''.join(code_list)
    return verification_code