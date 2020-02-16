from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .forms import UserRegisterForm
from util.JWT import  JWT
import json
from .models import  UserProfile
import hashlib
# Create your views here.
class Users(View):


    def post(self,request):
        """
        处理用户注册逻辑
        :param request:
        :return:
        """
        json_data = json.loads(request.body.decode())
        registerForm = UserRegisterForm(data=json_data)

        if registerForm.is_valid():
            username = registerForm.cleaned_data['username']
            user = UserProfile.objects.filter(username=username)

            if not user:

                md5 = hashlib.md5()
                md5.update(registerForm.cleaned_data['password1'].encode())
                password = md5.hexdigest()

                user = UserProfile.objects.create(username=username,password=password)
                user.save()

                payload = {'username':username}
                token = JWT.encode(payload,'kaoye17')
                res = {
                    'code':200,
                    'username':username,
                    'data':{'token':token.decode()}
                }
                return JsonResponse(res)

            else:
                res = {'code':207,'error':'用户名已经存在'}
                return JsonResponse(res)

        else:
            error = registerForm.errors
            res = {'code':201,'error':json.dumps(error.keys())}
            return JsonResponse(res)




        # if not register_data:
        #     res = {'code':202,'error':'请求中无内容'}
        #     return JsonResponse(res)

