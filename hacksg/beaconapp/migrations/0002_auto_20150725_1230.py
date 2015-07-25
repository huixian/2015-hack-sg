# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('beaconapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='node_name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reading',
            name='beacon_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 4, 30, 4, 927608, tzinfo=utc)),
        ),
    ]
