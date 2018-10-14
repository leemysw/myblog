from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    """ 分类 """
    name = models.CharField(verbose_name="文章类别", max_length=30)

    class Meta:
        verbose_name = "文章类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    """ 标签 """
    name = models.CharField(verbose_name="标签", max_length=20)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class View(models.Model):
    """网站统计"""
    ip = models.CharField(verbose_name='ip地址', max_length=20)
    ip_count = models.IntegerField(verbose_name='访问次数')
    ip_address = models.CharField(verbose_name='ip所属地', max_length=50, default="Not Found")
    view_time = models.CharField(verbose_name='访问时间', max_length=30)
    pv = models.IntegerField(verbose_name='网站点击量', default=0)
    uv = models.IntegerField(verbose_name='访客', default=0)

    def __str__(self):
        return self.ip_address


class Blog(models.Model):
    """  博客 """
    title = models.CharField(verbose_name='标题', max_length=100)
    content = RichTextUploadingField(verbose_name='正文', default='')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, related_name='blog', verbose_name='文章类别', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='blog', verbose_name='文章标签', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.TextField(verbose_name='摘要', blank=True)
    image_static = models.ImageField(verbose_name='首页配图', upload_to='./%Y', blank=True)
    image_url = models.CharField(verbose_name='图片链接', default='/', max_length=100, blank=True)
    image_author = models.CharField(verbose_name='图片作者', default='leemysw', max_length=300, blank=True)

    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('blog_detail', kwargs={'id': self.id})

    def increase_click(self):
        self.click_nums += 1
        self.save(update_fields=['click_nums'])
