# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20180306_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapons',
            name='attack',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='deattack',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='defence',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='dmg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='dmg_offset',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='focus',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='focus_offset',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='leather',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='steel',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='stun',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='wood',
            field=models.FloatField(),
        ),
    ]