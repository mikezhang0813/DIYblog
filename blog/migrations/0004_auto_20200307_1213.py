# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-07 12:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200307_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogBanner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='blogCategory',
            field=models.SmallIntegerField(null=True, verbose_name='博客类别'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogCreateTime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogModifyTime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
