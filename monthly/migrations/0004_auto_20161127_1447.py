# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-27 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly', '0003_auto_20161127_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budzetmax',
            name='expenditure_month',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='budzetmax',
            name='expenditure_year',
            field=models.IntegerField(default=2016),
        ),
        migrations.AlterField(
            model_name='budzetmax',
            name='expenduture_date',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]