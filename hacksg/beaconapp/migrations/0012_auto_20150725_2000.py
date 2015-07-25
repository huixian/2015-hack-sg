# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('beaconapp', '0011_auto_20150725_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reading',
            name='sequence',
        ),
        migrations.AlterField(
            model_name='reading',
            name='beacon_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 12, 0, 27, 840935, tzinfo=utc)),
        ),
    ]
