# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20180309_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventary',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventary',
            name='pos',
            field=models.IntegerField(unique=True),
        ),
    ]