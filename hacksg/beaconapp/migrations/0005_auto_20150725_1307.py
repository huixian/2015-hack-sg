# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import geoposition.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beaconapp', '0004_auto_20150725_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='node_location',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
        migrations.AlterField(
            model_name='reading',
            name='beacon_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 5, 7, 6, 960936, tzinfo=utc)),
        ),
    ]
