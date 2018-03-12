# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_armor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='armors',
            old_name='armor',
            new_name='dmg',
        ),
        migrations.AlterField(
            model_name='armor',
            name='static',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Armors'),
        ),
    ]
