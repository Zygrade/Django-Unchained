# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-29 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180313_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumnail',
            field=models.ImageField(blank=True, default='default.png', upload_to=b''),
        ),
    ]
