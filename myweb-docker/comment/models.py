from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# 从别的app中导入文章模型
from blog.models import Blog
from login.models import User


# Create your models here.

class BaseComment(models.Model):
    '基础评论模型'
    # content = models.TextField('评论', max_length=500)
    content = RichTextUploadingField(verbose_name='评论',config_name='comment')

    time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论者')

    class Meta:
        abstract = True

    def __str__(self):
        return self.content




class Comment(BaseComment):
    '文章评论'

    class Meta:
        ordering = ['-time']


class CommentReply(BaseComment):
    '文章评论回复(二级评论)'
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies', verbose_name='一级评论')
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='回复对象')

    class Meta:
        ordering = ['time']
