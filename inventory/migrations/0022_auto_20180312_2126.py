# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_auto_20180312_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='shields',
            new_name='shield',
        ),
    ]