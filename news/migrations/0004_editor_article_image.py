# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-11 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='article_image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='articles/'),
        ),
    ]
