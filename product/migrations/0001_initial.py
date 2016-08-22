# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-20 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CycleStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=36)),
                ('invalid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sap_no', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('product_desc', models.CharField(max_length=36)),
                ('specification', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=36)),
                ('invalid', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='cycle_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.CycleStatus'),
        ),
    ]
