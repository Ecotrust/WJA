# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='average_dbh',
            field=models.IntegerField(default=None, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatment',
            name='treated_acres',
            field=models.FloatField(default=None, blank=True, null=True),
            preserve_default=True,
        ),
    ]
