# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('node_id', models.IntegerField(verbose_name='NodeID')),
                ('node_location', geoposition.fields.GeopositionField(max_length=42, default=geoposition.fields.GeopositionField(max_length=42, verbose_name=0))),
            ],
        ),
        migrations.CreateModel(
            name='NodeType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type_id', models.PositiveSmallIntegerField(verbose_name='NodeType')),
                ('node_profile_type', models.PositiveSmallIntegerField(default=1, choices=[(0, 'BeaconNode'), (1, 'TagNode')])),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('server_timestamp', models.DateTimeField(auto_now_add=True)),
                ('beacon_timestamp', models.DateTimeField(default=datetime.datetime(2015, 7, 25, 0, 32, 52, 747168, tzinfo=utc))),
                ('sequence', models.PositiveIntegerField()),
                ('tagDesc', models.CharField(max_length=50, blank=True)),
                ('beaconLoc', geoposition.fields.GeopositionField(max_length=42, default=geoposition.fields.GeopositionField(max_length=42, verbose_name=0))),
                ('beacon', models.ForeignKey(related_name='beacon_reading', to='beaconapp.Node')),
                ('tag', models.ForeignKey(related_name='sensor_reading', to='beaconapp.Node')),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='node_type',
            field=models.ForeignKey(related_name='node', to='beaconapp.NodeType'),
        ),
    ]
