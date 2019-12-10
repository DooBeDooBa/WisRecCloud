# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-12-10 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=20, unique=True)),
                ('api_key', models.CharField(max_length=20, unique=True)),
                ('secret_key', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '客户数据表',
                'db_table': 'client_info',
            },
        ),
        migrations.CreateModel(
            name='JieCardData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.IntegerField()),
                ('digest', models.CharField(max_length=2000)),
                ('key_digest', models.CharField(blank=True, max_length=500)),
                ('indexer', models.CharField(choices=[('1', '完成'), ('0', '未完成')], max_length=4)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client', to='recall.ClientInfo')),
            ],
            options={
                'verbose_name_plural': '杰卡德数据表',
                'db_table': 'jie_card_data',
            },
        ),
    ]
