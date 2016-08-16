# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_materialctrloption_ordercategory_zmmsoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sap_no',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
