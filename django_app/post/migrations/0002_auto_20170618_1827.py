# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='post'),
        ),
    ]
