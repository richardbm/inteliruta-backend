# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 15:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0006_offer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 10, 15, 34, 12, 580526, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
