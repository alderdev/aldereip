# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0006_auto_20160817_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sap_no',
            field=models.CharField(max_length=18, primary_key=True, serialize=False),
        ),
    ]