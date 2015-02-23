# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=255, null=True, default='Failed', blank=True, choices=[('Successful', 'Successful'), ('Failed', 'Failed')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('unique_id', models.IntegerField(serialize=False, primary_key=True, unique=True)),
                ('data_source', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('project_name', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('ownership', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('access', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('treatment_date', models.DateField(blank=True, null=True, default=None)),
                ('treatment_type', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('treated_acres', models.FloatField(blank=True, null=True, default=None)),
                ('average_slope', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('current_status', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('tree_species', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('juniper_phase', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('average_dbh', models.IntegerField(blank=True, null=True, default=None)),
                ('tons_per_acre', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('contact_name', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('contact_email', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('contact_phone', models.CharField(max_length=255, null=True, default=None, blank=True)),
                ('batch', models.ForeignKey(blank=True, null=True, default=None, to='batch.Batch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
