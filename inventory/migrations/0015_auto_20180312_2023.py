# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20180310_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='armor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Armors'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='shields',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Shields'),
        ),
    ]