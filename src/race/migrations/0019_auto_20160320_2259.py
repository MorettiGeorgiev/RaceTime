# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0018_participant_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
