from django.urls import path

from . import views

urlpatterns = [
    path('aboutme/', views.about_me, name='about_me'),
    path('blog/', views.blog_list, name='blog_list')
]
