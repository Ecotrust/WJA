# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0004_auto_20150406_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentproject',
            name='batch',
            field=models.ForeignKey(to='ui.ImportEvent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatmentproject',
            name='contact_name',
            field=models.CharField(default=None, null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatmentproject',
            name='contact_phone',
            field=models.CharField(default=None, null=True, max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatmentproject',
            name='latitude',
            field=models.DecimalField(max_digits=20, null=True, default=None, blank=True, decimal_places=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatmentproject',
            name='longitude',
            field=models.DecimalField(max_digits=20, null=True, default=None, blank=True, decimal_places=16),
            preserve_default=True,
        ),
    ]
