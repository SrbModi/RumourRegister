# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login_data',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=120, unique=True)),
                ('password', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
