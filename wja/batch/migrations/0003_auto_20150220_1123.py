# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0002_auto_20150220_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatment',
            name='latitude',
            field=models.FloatField(blank=True, null=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatment',
            name='longitude',
            field=models.FloatField(blank=True, null=True, default=None),
            preserve_default=True,
        ),
    ]
