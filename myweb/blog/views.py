# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, Tag, View
from plan.models import Plan
import markdown
from .page import getPages
from .get_news import GetNews

"""首页"""


def index(request):
    blog_list = Blog.objects.all().order_by('-create_time')
    pages, blogs = getPages(request, blog_list)
    blog_list = blogs
    new = GetNews()
    try:
        new.get_news()
        news = new.news
    except:
        news = [{'edited_title': 'NOTHING',
                 'icon': '',
                 'summary': '一定是哪里出了问题',
                 'url': '',
                 'hour': '',
                 'time': '',
                 'color': '#fd1900'}]

    return render(request, 'blog/index.html', locals(), )


# 文章详情
def detail(request, id):
    blog = Blog.objects.get(id=id)
    blog.content = markdown.markdown(blog.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                         'fenced_code',
                                     ])
    click = Blog.objects.get(id=id)
    click.increase_click()
    return render(request, 'blog/blog.html', {'blog': blog})


# 归档
def archives(request, year, month):
    # 过滤条件
    blog_list = Blog.objects.filter(create_time__year=year,
                                    create_time__month=month).order_by('-create_time')
    pages, blogs = getPages(request, blog_list)
    blog_list = blogs
    return render(request, 'blog/index.html', locals())


# 分类
def category(request, id):
    cate = get_object_or_404(Category, id=id)
    blog_list = Blog.objects.filter(category=cate).order_by('-create_time')
    pages, blogs = getPages(request, blog_list)
    blog_list = blogs
    return render(request, 'blog/index.html', locals())


# 标签
def tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    blog_list = Blog.objects.filter(tag=tag).order_by('-create_time')
    pages, blogs = getPages(request, blog_list)
    blog_list = blogs
    return render(request, 'blog/index.html', locals())


# about me
def about_me(request, ):
    return render(request, 'blog/about.html')


def test(request, ):
    return render(request, 'blog/test.html', locals())


def search(request):
    q = request.GET.get('q')
    blog_list = Blog.objects.filter(content__icontains=q)
    pages, blogs = getPages(request, blog_list)
    blog_list = blogs

    return render(request, 'blog/index.html', locals())
