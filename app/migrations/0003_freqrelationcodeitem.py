# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_relationcodeitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreqRelationCodeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_type', models.CharField(max_length=100)),
                ('end_type', models.CharField(max_length=100)),
                ('link_type', models.CharField(max_length=100)),
                ('freq', models.BigIntegerField(default=0)),
                ('code_test_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CodeTestItem')),
            ],
        ),
    ]