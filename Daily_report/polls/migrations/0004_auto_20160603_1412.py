# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 05:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160603_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 3, 5, 12, 13, 574381, tzinfo=utc), verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 3, 5, 12, 13, 573381, tzinfo=utc), verbose_name='日付'),
        ),
    ]
