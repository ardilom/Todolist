# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 00:37
from __future__ import unicode_literals

import appTodolist.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTodolist', '0005_auto_20170505_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=appTodolist.models.new_priority),
        ),
    ]
