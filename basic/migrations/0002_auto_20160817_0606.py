# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='sap_no',
            field=models.BigIntegerField(serialize=False, max_length=36, primary_key=True),
        ),
    ]
