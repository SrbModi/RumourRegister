# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0002_add_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_data',
            name='flag',
            field=models.SmallIntegerField(default=0),
        ),
    ]