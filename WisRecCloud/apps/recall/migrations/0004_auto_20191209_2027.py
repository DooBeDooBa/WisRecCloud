# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-12-09 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recall', '0003_auto_20191209_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jiecarddata',
            name='data_id',
            field=models.IntegerField(),
        ),
    ]
