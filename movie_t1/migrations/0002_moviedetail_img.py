# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_t1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetail',
            name='img',
            field=models.ImageField(default=None, null=True, upload_to='movie'),
        ),
    ]
