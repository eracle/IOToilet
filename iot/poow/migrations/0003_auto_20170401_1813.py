# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poow', '0002_auto_20170401_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poo',
            name='uuid',
            field=models.CharField(db_index=True, max_length=5),
        ),
    ]