# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-12-10 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recall', '0002_auto_20191210_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jiecarddata',
            name='digest',
        ),
    ]
