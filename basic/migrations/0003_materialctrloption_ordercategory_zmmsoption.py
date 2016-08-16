# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20160817_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialCtrlOption',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=36)),
                ('invalid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=36)),
                ('order_squence', models.IntegerField(default=1000)),
                ('invalid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ZmmsOption',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=36)),
                ('invalid', models.BooleanField(default=False)),
            ],
        ),
    ]
