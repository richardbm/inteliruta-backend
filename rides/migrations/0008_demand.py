# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 15:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0007_offer_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField(blank=True, null=True)),
                ('condition', models.CharField(choices=[('PS', 'Por puesto'), ('FC', 'Auto completo')], default='PS', max_length=2)),
                ('seats', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('Di', 'Disponible'), ('Re', 'Reservado'), ('Ca', 'Cancelado'), ('Re', 'Realizado')], default='Di', max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('arrival_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_arrival', to='rides.Address')),
                ('departure_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_address', to='rides.Address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]