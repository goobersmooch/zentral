# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-05 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160504_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(default='0079bf', max_length=6),
        ),
    ]
