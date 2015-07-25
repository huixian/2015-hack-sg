# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beaconapp', '0005_auto_20150725_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='node_location',
            field=geoposition.fields.GeopositionField(max_length=42, default=geoposition.fields.GeopositionField(verbose_name=0, max_length=42)),
        ),
        migrations.AlterField(
            model_name='reading',
            name='beacon_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 5, 9, 59, 188277, tzinfo=utc)),
        ),
    ]
