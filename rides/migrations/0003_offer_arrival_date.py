# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 12:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_address_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 10, 12, 52, 0, 224002, tzinfo=utc)),
            preserve_default=False,
        ),
    ]