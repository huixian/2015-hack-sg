# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beaconapp', '0010_auto_20150725_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='beacon_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 6, 55, 50, 510532, tzinfo=utc)),
        ),
    ]
