# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-12-12 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recall', '0004_clientinfo_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieCFData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('movie_id', models.IntegerField()),
                ('ratting', models.FloatField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client_id', to='recall.ClientInfo')),
            ],
            options={
                'verbose_name_plural': '杰卡德数据表',
                'db_table': 'movie_cf_data',
            },
        ),
    ]
