# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(max_length=50)),
                ('number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('fbpagelink', models.URLField()),
                ('address', models.TextField()),
                ('meetuplink', models.URLField()),
            ],
        ),
    ]
