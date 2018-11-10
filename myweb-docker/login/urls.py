from django.urls import path, include

from login import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
    path('captcha/', include('captcha.urls')),
    # path('confirm/', views.confirm, name='confirm'),
    # path('confirm_code/', views.confirm_code, name='confirm_code'),
    path('user/', views.user_home, name='user_home'),
]
