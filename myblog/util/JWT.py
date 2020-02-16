import hmac
import base64
import copy
import json
import jwt
import time
class JWT():
    @staticmethod
    def encode(payload,key,exp=60*60*24):
        if not isinstance(key,bytes):
            key = key.encode()
        header = {'alg':'HS256','typ':'JWT'}
        #可变类型需要深拷贝防止变量污染
        payload = copy.deepcopy(payload)
        payload['exp'] = time.time()+exp
        to_encry = JWT._base64_encode(json.dumps(header,separators=(',',':'),sort_keys=True).encode())+b'.'+\
                                 JWT._base64_encode(json.dumps(payload,separators=(',',':'),sort_keys=True).encode())

        token = hmac.new(key,to_encry,digestmod='SHA256').digest()
        return to_encry+b'.'+JWT._base64_encode(token)
    @staticmethod
    def _base64_encode(sign):
        half_token = base64.urlsafe_b64encode(sign).replace(b'=',b'')
        #将多余的=替换为空格节省储存空间

        return half_token
    @staticmethod
    def decode(key,token):
        if not isinstance(key,bytes):
            key = key.encode()
        header,payload,sign = token.split(b'.')

        generated_in_server = hmac.new(key,header+b'.'+payload,digestmod='SHA256').digest()
        generated_in_server = JWT._base64_encode(generated_in_server)

        header,payload,sign_from_browser = JWT._base64_decode(header),JWT._base64_decode(payload),sign
        result = JWT.is_token_valid(sign_from_browser,generated_in_server,payload)
        return result,payload
    @staticmethod
    def is_token_valid(token_from_browser,token_in_server,payload):
        result = {}
        if  isinstance(payload,bytes):
            payload = json.loads(payload.decode())
        if token_from_browser == token_in_server:
            if time.time()>payload['exp']:
                result['code']=201
                result['error'] ='pass due'
            else:
                result['code'] = 200
                result['error']=""
        else:
            result['code'] = 403
            result['error'] = 'token not match'

        return result




    @staticmethod
    def _base64_decode(sign):
        if len(sign)%4!=0:
            sign +=b"="*(4-len(sign)%4)
        sign = base64.urlsafe_b64decode(sign)

        return sign



if __name__ == "__main__":
    payload = {
        'username':'mikezhang'
    }
    token = JWT.encode(payload,'kaoye17')
    result,payload=JWT.decode('kaoye17',token)
    print(result,payload)