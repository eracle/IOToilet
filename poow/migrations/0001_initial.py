# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=5)),
                ('timestamp', models.FloatField()),
                ('sensor_fr', models.FloatField()),
                ('sensor_fl', models.FloatField()),
                ('sensor_br', models.FloatField()),
                ('sensor_bl', models.FloatField()),
            ],
        ),
    ]