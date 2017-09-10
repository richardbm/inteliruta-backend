# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 20:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0017_offer_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='demand',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='rides.Demand'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='passenger',
            field=models.ManyToManyField(blank=True, related_name='passenger_offer', to=settings.AUTH_USER_MODEL),
        ),
    ]