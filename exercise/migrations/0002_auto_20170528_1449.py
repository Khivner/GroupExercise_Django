# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='reps',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=7, null=True),
        ),
    ]