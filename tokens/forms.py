from django import forms



class DynaticLoginForm(forms.Form):
    mobile = forms.CharField(min_length=11,max_length=11,required=True)

    veri_code = forms.CharField(min_length=4,max_length=4,required=True)

class LoginForm(forms.Form):
    username = forms.CharField(min_length=5,required=True)
    password=  forms.CharField(min_length=8,required=True)