# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0008_demand'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='demand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='rides.Demand'),
        ),
    ]
