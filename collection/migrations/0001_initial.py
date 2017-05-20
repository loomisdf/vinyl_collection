# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(verbose_name='date added to database')),
                ('last_modified', models.DateTimeField(verbose_name='last time updated')),
                ('resale_value', models.DecimalField(decimal_places=2, max_digits=19)),
                ('paid_value', models.DecimalField(decimal_places=2, max_digits=19)),
                ('album_name', models.CharField(max_length=200)),
                ('artist_name', models.CharField(max_length=200)),
                ('skips', models.IntegerField(default=0)),
                ('sleeve_quality', models.CharField(max_length=20)),
                ('vinyl_quality', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]