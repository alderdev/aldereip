# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='category',
            field=models.ForeignKey(to='basic.OrderCategory'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='material_ctrl',
            field=models.ForeignKey(null=True, to='basic.MaterialCtrlOption', blank=True),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='zmms',
            field=models.ForeignKey(null=True, to='basic.ZmmsOption', blank=True),
        ),
        migrations.DeleteModel(
            name='MaterialCtrlOption',
        ),
        migrations.DeleteModel(
            name='OrderCategory',
        ),
        migrations.DeleteModel(
            name='ZmmsOption',
        ),
    ]
