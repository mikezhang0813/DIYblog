from django.shortcuts import render
from util.JWT import  JWT
from util.yunpian import send_sms,generate_number
from django.views.generic import View
from .forms import DynaticLoginForm,LoginForm
from django.http import  JsonResponse
from django.contrib.auth import authenticate
from users.models import  UserProfile
import json
import  hashlib
# Create your views here.


class LoginView(View):
    def post(self,request):
        json_data = json.loads(request.body.decode())
        if not json_data:
            res = {'code':206,'error':'请求中无内容'}
            return JsonResponse(res)

        user_form = LoginForm(json_data)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = UserProfile.objects.filter(username=username)

            if user  is not None:
                '''用户存在'''
                print(user[0].password)
                print(password)
                stored_password = user[0].password
                m5 = hashlib.md5()
                m5.update(password.encode('utf8'))
                new_password = m5.hexdigest()
                print(new_password)
                if stored_password == m5.hexdigest():

                    payload = {'username':username}
                    token = JWT.encode(payload,'kaoye17')
                    res = {'code':200,'username':username,'data':{'token':token.decode()}}
                    return JsonResponse(res)
                else:
                    res = {'code':205,'error':'用户名或密码错误'}
                    return JsonResponse(res)
            else:
                res = {'code':206,'error':'用户名或密码错误'}
                return JsonResponse(res)



class DynaticLoginView(View):
    def post(self,request):
        json_data = request.body
        if not json_data:
            res = {'code':301,'error':'请求为空'}
            return JsonResponse(res)
        form_data = DynaticLoginForm(request.body.decode())

        if form_data.is_valid():
            mobile = form_data.cleaned_data['mobile']
            code = generate_number()
            result =send_sms(code,mobile)
            print(result)



