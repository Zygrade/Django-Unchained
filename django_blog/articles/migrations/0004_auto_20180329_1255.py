# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-29 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_thumnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumnail',
            new_name='thumbnail',
        ),
    ]
