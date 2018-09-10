from django.test import TestCase

# Create your tests here.

from blog.models import Blog,View,Tag,Category

tag_list = Tag.objects.all()