# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('race', '0002_remove_race_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish_time', models.TimeField()),
                ('avg_speed', models.DecimalField(decimal_places=2, max_digits=4)),
                ('avg_pulse', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_pulse', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cadence', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='distance',
            field=models.FloatField(default=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.Race'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
