# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0007_auto_20160817_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotehead',
            name='currency',
            field=models.ForeignKey(default='TWD', on_delete=django.db.models.deletion.CASCADE, to='ship.Currency'),
            preserve_default=False,
        ),
    ]