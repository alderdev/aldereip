# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_auto_20160817_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sap_no',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
    ]
