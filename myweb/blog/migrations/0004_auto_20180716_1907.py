# Generated by Django 2.0.6 on 2018-07-16 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180715_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='number',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='number',
        ),
    ]
