# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('beaconapp', '0005_auto_20150725_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='node_location',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='beaconLoc',
        ),
        migrations.AddField(
            model_name='node',
            name='node_lat',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='node',
            name='node_lon',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='reading',
            name='beacon_lat',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='reading',
            name='beacon_lon',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='reading',
            name='beacon_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 6, 45, 59, 708578, tzinfo=utc)),
        ),
    ]
