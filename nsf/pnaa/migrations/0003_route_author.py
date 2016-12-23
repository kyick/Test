# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-22 21:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pnaa', '0002_auto_20161222_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
