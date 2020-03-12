import jwt
from .JWT import JWT
import json
from django.http import JsonResponse
from users.models import UserProfile
def login_check(func):
    def wrapper(request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        # print(request.body.decode('utf8'))
        username = json.loads(request.body.decode()).get('username',None)
        if not token or not username:
            res = {'code':403,'error':'please login first'}
            return JsonResponse(res)
        try:
            result,payload = JWT.decode('kaoye17',token)
            username_in_token = json.loads(payload.decode()).get('username',None)
            if username != username:
                res = {'code':403,'error':'illegal request found'}
                return JsonResponse(res)
        except Exception as e:
            print("login_check",e)
            res = {'code': 500, 'error': 'server error'}
            return JsonResponse(res)
        else:
            if result['code'] == 200:
                if not isinstance(payload,str):
                    payload =json.loads(payload.decode())
                username = payload.get('username',None)
                if username:
                    try:
                        user = UserProfile.objects.get(username=username)
                    except Exception as e:
                        res = {'code':402,'error':'please register first'}
                        return JsonResponse(res)
                    request.user = user
                    return func(request,*args,**kwargs)
                else:
                    res = {'code':402,'error':'please register first'}
                    return JsonResponse(res)
            else:
                res = {'code':405,'error':'please login first'}
                return  JsonResponse(res)







    return wrapper

