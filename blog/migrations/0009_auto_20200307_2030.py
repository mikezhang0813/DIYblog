# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-07 12:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200307_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogCreateTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 7, 12, 30, 37, 609072, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogModifyTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 7, 12, 30, 37, 609186, tzinfo=utc), null=True),
        ),
    ]
