# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20160911_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentstatus',
            name='Reason',
            field=models.CharField(default='none', max_length=1000),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='Mentor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='MentorEmail',
            field=models.CharField(max_length=100),
        ),
    ]
