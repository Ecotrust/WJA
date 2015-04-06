# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0003_auto_20150406_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentproject',
            name='average_dbh',
            field=models.IntegerField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatmentproject',
            name='batch',
            field=models.ForeignKey(to='ui.ImportEvent', null=True, default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatmentproject',
            name='contact_email',
            field=models.EmailField(null=True, default=None, blank=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='treatmentproject',
            name='treated_acres',
            field=models.IntegerField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
    ]
