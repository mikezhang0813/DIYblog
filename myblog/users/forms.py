from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True,min_length=8)
    mail = forms.EmailField(required=True)
    password1= forms.CharField(required=True,min_length=10,widget=forms.PasswordInput)
    password2 =forms.CharField(required=True,min_length=10,widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']

        return self.cleaned_data['username']


    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise  forms.ValidationError('密码不一致')
        return self.cleaned_data
class UserloginForm(forms.Form):
    username = forms.CharField(min_length=5,required=True)
    password = forms.CharField(min_length=8,required=True)



