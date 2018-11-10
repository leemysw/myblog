import os

from django.core.mail import EmailMultiAlternatives

# from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


def send_email(send_to, code):
    subject, from_email, to = '来自www.leemysw.top的验证邮件', 'leemysw@sina.com', send_to
    text_content = '欢迎访问www.leemysw.top'
    html_content = '<p>感谢注册<a href="https://www.leemysw.top/confirm/?code={}" target=blank>www.leemysw.top</a>,</p>' \
                   '<p>此链接有效期为7天！</p>'.format(code)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

#
# if __name__ == '__main__':
#     send_email('leemysw@163.com')


# send_mail(
#     '来自www.leemysw.top的测试邮件',
#     '欢迎访问www.leemysw.top，',
#     'leemysw@sina.com',
#     ['leemysw@163.com'],
# )
