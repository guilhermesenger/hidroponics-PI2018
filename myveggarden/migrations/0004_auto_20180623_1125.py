# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-06-23 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myveggarden', '0003_garden_temperature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garden',
            old_name='cycle_time',
            new_name='last_update',
        ),
    ]
