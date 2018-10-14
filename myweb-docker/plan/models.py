from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
# Create your models here.
class Plan(models.Model):
    plan = models.CharField(verbose_name='计划', max_length=200)
    detail = RichTextUploadingField(verbose_name='细节', default='', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建日期', default=timezone.now)
    sys = models.CharField(verbose_name='符号', choices=(
        ('fa fa-check', '完成'),
        ('fa fa-times', '未完成'),
    ), max_length=50)
    author = models.ForeignKey(User, on_delete=True, default='leemysw')

    class Meta:
        verbose_name = "计划"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.plan
