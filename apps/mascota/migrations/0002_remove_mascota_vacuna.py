# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-11-07 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='vacuna',
        ),
    ]