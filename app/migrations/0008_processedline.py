# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20161019_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smother_name', models.CharField(max_length=100)),
                ('line_source', models.TextField()),
                ('line_test', models.TextField()),
            ],
        ),
    ]
