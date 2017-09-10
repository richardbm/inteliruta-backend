# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0008_requestpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestpost',
            name='offer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rides.Offer'),
            preserve_default=False,
        ),
    ]
