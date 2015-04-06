# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_auto_20150403_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentproject',
            name='treatment_date',
            field=models.DateTimeField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
