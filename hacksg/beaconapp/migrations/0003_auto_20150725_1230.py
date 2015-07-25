# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beaconapp', '0002_auto_20150725_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='node_name',
            field=models.CharField(max_length=100, default='null'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='beacon_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 4, 30, 56, 516201, tzinfo=utc)),
        ),
    ]
