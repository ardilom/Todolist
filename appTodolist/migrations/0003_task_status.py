# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-23 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTodolist', '0002_auto_20170320_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
