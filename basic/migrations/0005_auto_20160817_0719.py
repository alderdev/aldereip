# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20160817_0629'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=36)),
                ('invalid', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, to='basic.ProductCategory'),
            preserve_default=False,
        ),
    ]
