# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-11 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190611_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editor',
            name='article_image',
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='articles/'),
        ),
    ]
