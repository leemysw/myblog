from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=20, choices=(('default', '保密'), ('male', '男'), ('female', '女')), default='保密')
    c_time = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False)
    code = models.CharField(max_length=256)
    code_time = models.DateTimeField(default=timezone.now)

    def is_authenticated(self):
        return True

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = "用户"
        verbose_name_plural = "用户"