# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_auto_20180312_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('quality', models.IntegerField()),
                ('static', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Shields')),
            ],
        ),
    ]
