# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_freqrelationcodeitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='codetestitem',
            name='depth_code',
            field=models.IntegerField(default=0),
        ),
    ]