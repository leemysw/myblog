from captcha.fields import CaptchaField
from django.forms import ModelForm, TextInput, PasswordInput, Form, EmailInput

from .models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        exclude = ('c_time', 'sex', 'email', 'confirmed', 'code', 'code_time')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control ', 'autofocus': True, 'value': 'input name',
                                     'onfocus': 'if(this.value=="input name"){this.value="";}; ',
                                     'onblur': 'if(this.value==""){this.value="input name";};'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'autocomplete': "new-password"}),
            # 'email':EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': '名字',
            'password': '密码',
            # 'email':'邮箱',
        }


class RegisterForm(ModelForm):
    class Meta:
        model = User
        exclude = ('c_time', 'confirmed', 'code', 'code_time')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control ', 'autofocus': True, 'value': 'input name',
                                     'onfocus': 'if(this.value=="input name"){this.value="";}; ',
                                     'onblur': 'if(this.value==""){this.value="input name";};'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'autocomplete': "new-password"}),
            # 'sex': ChoiceField(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
        }
        labels = {
            'name': '名字',
            'password': '密码',
            'email': '邮箱',
            'sex': '性别',
        }


class CaptchaForm(Form):
    captcha = CaptchaField(label='验证码')
