# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0004_shiporderdetail_unitprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='sap_no',
            field=models.BigIntegerField(serialize=False, max_length=36, primary_key=True),
        ),
    ]
