# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 08:55
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('area', models.CharField(choices=[(b'techniques', 'Techniques'), (b'tools', 'Tools'), (b'platforms', 'Platforms'), (b'languages_frameworks', 'Languages & Frameworks')], max_length=32)),
                ('status', models.CharField(choices=[(b'access', 'Access'), (b'trial', 'Trial'), (b'adopt', 'Adopt'), (b'on_hold', 'On hold')], max_length=16)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name')),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalBlip',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('area', models.CharField(choices=[(b'techniques', 'Techniques'), (b'tools', 'Tools'), (b'platforms', 'Platforms'), (b'languages_frameworks', 'Languages & Frameworks')], max_length=32)),
                ('status', models.CharField(choices=[(b'access', 'Access'), (b'trial', 'Trial'), (b'adopt', 'Adopt'), (b'on_hold', 'On hold')], max_length=16)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name')),
                ('body', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical blip',
            },
        ),
        migrations.CreateModel(
            name='Radar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='historicalblip',
            name='radar',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='technology_radar.Radar'),
        ),
        migrations.AddField(
            model_name='blip',
            name='radar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blips', to='technology_radar.Radar'),
        ),
    ]
