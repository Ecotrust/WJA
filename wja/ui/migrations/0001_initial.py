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
            name='ImportEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='unknown', max_length=255, choices=[('complete', 'Complete'), ('failed', 'Failed'), ('running', 'Running'), ('pending', 'Pending'), ('unknown', 'Unknown')])),
                ('notes', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TreatmentProject',
            fields=[
                ('unique_id', models.IntegerField(serialize=False, primary_key=True)),
                ('data_source', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('ownership', models.CharField(default='Unknown', max_length=255, choices=[('BLM', 'BLM'), ('Private', 'Private'), ('State', 'State'), ('Tribal', 'Tribal'), ('USFS', 'USFS'), ('USFWS', 'USFWS'), ('Other', 'Other'), ('Unknown', 'Unknown')])),
                ('access', models.CharField(default='Unknown', max_length=255, choices=[('Public', 'Public'), ('Private', 'Private'), ('Mixed', 'Mixed'), ('Other', 'Other'), ('Unknown', 'Unknown')])),
                ('treatment_date', models.DateTimeField()),
                ('treatment_type', models.CharField(default='Unknown', max_length=255, choices=[('Lop and scatter', 'Lop and scatter'), ('Manual thin and pile', 'Manual thin and pile'), ('Mechanical thin and pile', 'Mechanical thin and pile'), ('Mechanical thin and scatter', 'Mechanical thin and scatter'), ('Mechanical thin and yard', 'Mechanical thin and yard')])),
                ('treated_acres', models.IntegerField()),
                ('average_slope', models.CharField(default='Unknown', max_length=255, choices=[('0', '0'), ('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('>40', '>40'), ('Unknown', 'Unknown')])),
                ('current_status', models.CharField(default='Unknown', max_length=255, choices=[('Still standing', 'Still standing'), ('Cut', 'Cut'), ('Piled', 'Piled'), ('Unknown', 'Unknown')])),
                ('tree_species', models.CharField(default='Western Juniper', max_length=255)),
                ('juniper_phase', models.CharField(default='Unknown', max_length=255, choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('Unknown', 'Unknown')])),
                ('average_dbh', models.IntegerField()),
                ('tons_per_acre', models.CharField(default='Unknown', max_length=255, choices=[('1-3', '1-3'), ('3-5', '3-5'), ('5-7', '5-7'), ('7-10', '7-10'), ('10-13', '10-13'), ('13-15', '13-15'), ('>15', '>15'), ('Unknown', 'Unknown')])),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=20)),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=75)),
                ('contact_phone', models.CharField(max_length=30, blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=None, null=True, blank=True, srid=3857)),
                ('batch', models.ForeignKey(to='ui.ImportEvent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
