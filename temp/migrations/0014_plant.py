# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0013_decide_moto1_moto2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantName', models.CharField(default='Plant', max_length=100)),
                ('plantLatitude', models.FloatField(default=0)),
                ('plantLongitude', models.FloatField(default=0)),
            ],
        ),
    ]
