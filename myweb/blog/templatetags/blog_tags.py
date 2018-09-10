from ..models import Blog, Category, View, Tag
from plan.models import Plan
from django.db.models.aggregates import Count
from django import template

register = template.Library()

@register.simple_tag
def get_recent_blogs(num = 3):
    return Blog.objects.all().order_by('-click_nums')[:num]

@register.simple_tag
def archives():
    return Blog.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_blog=Count('blog')).filter(num_blog__gt=0)

@register.simple_tag
def get_tag():
    return Tag.objects.annotate(num_blog=Count('blog')).filter(num_blog__gt=0)

@register.simple_tag
def get_pvuv():
    return View.objects.last()
@register.simple_tag
def get_plan():
    return Plan.objects.all().order_by('-create_time')[:5]

