# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitycrmapp', '0002_auto_20160525_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='number',
            field=models.CharField(max_length=12),
        ),
    ]
