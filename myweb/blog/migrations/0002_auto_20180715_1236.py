# Generated by Django 2.0.6 on 2018-07-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_author',
            field=models.CharField(default='', max_length=300, verbose_name='图片作者'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image_static',
            field=models.ImageField(default='', upload_to='./%Y', verbose_name='首页配图'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image_url',
            field=models.CharField(default='', max_length=100, verbose_name='图片链接'),
        ),
    ]
