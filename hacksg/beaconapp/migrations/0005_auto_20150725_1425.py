# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('beaconapp', '0004_auto_20150725_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='beacon_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 6, 25, 12, 18668, tzinfo=utc)),
        ),
    ]
