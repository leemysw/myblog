from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View

from myweb.send_email import send_email
from .form import LoginForm, CaptchaForm, RegisterForm
from .func import hash_code, make_confirm_code
from .models import User
from django.utils import timezone

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


# Create your views here.

class Login(View):

    def get(self, request):
        if request.session.get('is_login', None):
            # name = request.session.get('user_name')
            # user = User.objects.get(name=name)
            # confirmed = user.confirmed
            redirect_to = request.GET.get('next', '/user')
            return redirect(redirect_to)

        login_form = LoginForm()
        captcha_form = CaptchaForm()
        return render(request, 'login/login.html', locals())


    #
    def post(self, request):
        login_form = LoginForm(request.POST)
        captcha_form = CaptchaForm(request.POST)
        if login_form.is_valid():
            name = login_form.cleaned_data['name']
            password = login_form.cleaned_data['password']

            try:
                user = User.objects.get(name=name)
                if user.password != hash_code(password):
                    message = '密码不正确'
                    return render(request, 'login/login.html', locals())
                elif not captcha_form.is_valid():
                    message = '验证码错误'
                    return render(request, 'login/login.html', locals())
                else:
                    request.session['is_login'] = True
                    request.session['user_name'] = user.name
                    if user.confirmed:
                        request.session['is_confirm'] = True
                    else:
                        request.session['is_confirm'] = False

                    redirect_to = request.GET.get('next', '/user')
                    return redirect(redirect_to)
            except:
                message = '用户不存在'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
        # name = request.POST.get('name', None)
        # password = request.POST.get('password', None)
        # email = request.POST.get('email')
        # captcha_form = CaptchaForm(request.POST)
        # if name and password and email:  # 确保用户名和密码都不为空
        #     name = name.strip()
        #     try:
        #         user = User.objects.get(name=name)
        #         if user.password != password:
        #             message = '密码不正确'
        #             return render(request, 'login.html', locals())
        #         elif user.email != email:
        #             message = '邮件不正确'
        #             return render(request, 'login.html', locals())
        #         elif not captcha_form.is_valid():
        #             message= '验证码错误'
        #             return render(request, 'login.html', locals())
        #         else:
        #             request.session['is_login'] = True
        #             request.session['user_id'] = user.id
        #             request.session['user_name'] = user.name
        #             return redirect('/')
        #     except:
        #         message = '用户不存在'
        #         return render(request, 'login.html', locals())


class Register(View):

    def get(self, request):
        if request.session.get('is_login', None):
            # name = request.session.get('user_name')
            # user = User.objects.get(name=name)
            # confirmed = user.confirmed
            redirect_to = request.GET.get('next', '/user')
            return redirect(redirect_to)

        register_form = RegisterForm()
        captcha_form = CaptchaForm()
        return render(request, 'login/register.html', locals())

    def post(self, request):
        register_form = RegisterForm(request.POST)
        captcha_form = CaptchaForm(request.POST)
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']

            user = User.objects.filter(name=name)
            user_email = User.objects.filter(email=email)
            if user:
                message = '用户已经存在，请重新选择用户名！'
                return render(request, 'login/register.html', locals())

            elif user_email:
                message = '该邮箱地址已被注册，请使用别的邮箱！'
                return render(request, 'login/register.html', locals())

            elif not captcha_form.is_valid():
                message = '验证码错误'
                return render(request, 'login/register.html', locals())

            else:

                new_user = User()
                new_user.name = name
                new_user.password = hash_code(password)
                new_user.email = email
                new_user.sex = sex
                code = make_confirm_code()
                new_user.code = code
                new_user.save()
                send_email(email, code)

                request.session['is_login'] = True
                request.session['user_name'] = new_user.name
                request.session['is_confirm'] = False
                redirect_to = request.GET.get('next', '/user')
                return redirect(redirect_to)
        else:

            message = register_form.errors
            return render(request, 'login/register.html', locals())


def logout(request):

    if not request.session.get('is_login', None):
        return redirect("/")

    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/")


def user_home(request):
    if request.session.get('is_login', None):
        if request.GET.get('get_code'):
            name = request.session.get('user_name')
            user = User.objects.get(name=name)
            now = timezone.now()
            code_time = user.code_time
            if now < code_time + timezone.timedelta(7):
                message = '验证码未过期，若丢失请联系leemysw'
                return render(request, 'login/user_home.html', locals())
            else:
                code = make_confirm_code()
                user.code = code
                user.code_time = now
                user.save()
                message = '验证码已发送，请查收'
                return render(request, 'login/user_home.html', locals())
        elif request.GET.get('code'):
            code = request.GET.get('code')
            message = ''
            try:
                user = User.objects.get(code=code)
            except:
                message = '无效的确认请求'
                data = {}
                data['message'] = message
                return render(request, 'login/user_home.html', locals())

            now = timezone.now()
            code_time = user.code_time
            if now > code_time + timezone.timedelta(7):
                message = '请重新获取验证码'
                return render(request, 'login/user_home.html', locals())
            else:
                user.confirmed = True
                user.save()
                request.session['is_confirm'] = True
                message = '你的账号已验证'
                redirect_to = request.GET.get('next', '/user')
                return redirect(redirect_to)

        return render(request, 'login/user_home.html', locals())

    else:
        return redirect('/login')



# def confirm(request):
#     code = request.GET.get('code')
#     message = ''
#     try:
#         user =User.objects.get(code=code)
#     except:
#         message = '无效的确认请求'
#         return render(request, 'user_home.html', locals())
#
#     now = timezone.now()
#     code_time = user.code_time
#     if now > code_time + timezone.timedelta(7):
#         message = '请重新获取验证码'
#         return render(request, 'user_home.html', locals())
#     else:
#         user.confirmed = True
#         user.save()
#         request.session['is_confirm'] = True
#         message = '你的账号已验证'
#         return redirect('/user')


# def confirm_code(request):
#     name = request.session.get('user_name')
#     user =User.objects.get(name=name)
#     now = timezone.now()
#     code_time = user.code_time
#     if now < code_time + timezone.timedelta(7):
#         message = '验证码未过期，若丢失请联系leemysw'
#         return render(request, 'user_home.html', locals())
#     else:
#         code = make_confirm_code()
#         user.code = code
#         user.code_time = now
#         user.save()
#         message = '验证码已发送，请查收'
#         return render(request, 'user_home.html', locals())


