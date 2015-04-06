# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importevent',
            name='notes',
            field=models.TextField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
