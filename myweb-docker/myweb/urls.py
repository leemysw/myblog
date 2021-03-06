"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog import views as blog_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', blog_view.index, name='homepage'),
                  path('blog/<int:id>/', blog_view.detail, name='blog_detail'),
                  path('tag/<int:id>/', blog_view.tag, name='blog_tags'),
                  path('category/<int:id>/', blog_view.category, name='blog_category'),
                  path('archives/<int:year>/<int:month>', blog_view.archives, name='blog_archives'),
                  path('about/', blog_view.about_me, name='blog_about'),
                  path('', include('ckeditor_uploader.urls')),
                  path('search/', blog_view.search, name='blog_search'),
                  path('test/', blog_view.test, name='blog_test'),
                  path('', include('api.urls')),
                  path('', include('blog.urls')),
                  path('', include('login.urls')),
                  path('', include('comment.urls')),
                  # path('aboutme/', blog_view.about_me, name='about_me')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
