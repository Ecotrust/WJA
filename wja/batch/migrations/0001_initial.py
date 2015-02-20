# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('notes', models.TextField(default='', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=255, choices=[('Successful', 'Successful'), ('Failed', 'Failed')], default='Failed', blank=True, null=True)),
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
                ('data_source', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('project_name', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('ownership', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('access', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('treatment_date', models.DateField(default=None, blank=True, null=True)),
                ('treatment_type', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('treated_acres', models.FloatField()),
                ('average_slope', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('current_status', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('tree_species', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('juniper_phase', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('average_dbh', models.IntegerField()),
                ('tons_per_acre', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('contact_name', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('contact_email', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('contact_phone', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('batch', models.ForeignKey(default=None, to='batch.Batch', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
