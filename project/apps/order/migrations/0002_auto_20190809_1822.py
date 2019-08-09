# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-09 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('wait', 'wait'), ('cancel', 'cancel'), ('success', 'success')], default='wait', max_length=20),
        ),
    ]
