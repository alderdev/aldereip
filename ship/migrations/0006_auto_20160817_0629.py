# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0005_auto_20160817_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sap_no',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
