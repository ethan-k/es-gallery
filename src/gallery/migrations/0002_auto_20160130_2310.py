# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='photos'),
        ),
    ]