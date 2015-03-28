from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.gis.geos import Point
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from pytz import timezone
import pytz


class TreatmentProject(models.Model):
    # Django model representing a point where a treatment occurred

    ownershipChoices = (
        ('BLM', 'BLM'),
        ('Private', 'Private'),
        ('State', 'State'),
        ('Tribal', 'Tribal'),
        ('USFS', 'USFS'),
        ('USFWS', 'USFWS'),
        ('Other', 'Other'),
        ('Unknown', 'Unknown')
    )

    accessChoices = (
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Mixed', 'Mixed'),
        ('Other', 'Other'),
        ('Unknown', 'Unknown')
    )

    treatmentChoices = (
        ("Lop and scatter", "Lop and scatter"),
        ("Manual thin and pile", "Manual thin and pile"),
        ("Mechanical thin and pile", "Mechanical thin and pile"),
        ("Mechanical thin and scatter", "Mechanical thin and scatter"),
        ("Mechanical thin and yard", "Mechanical thin and yard")
    )

    slopeChoices = (
        ('0', '0'),
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
        ('>40', '>40'),
        ('Unknown', 'Unknown')
    )

    statusChoices = (
        ('Still standing', 'Still standing'),
        ('Cut', 'Cut'),
        ('Piled', 'Piled'),
        ('Unknown', 'Unknown')
    )

    phaseChoices = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('Unknown', 'Unknown')
    )

    densityChoices = (
        ('1-3', '1-3'),
        ('3-5', '3-5'),
        ('5-7', '5-7'),
        ('7-10', '7-10'),
        ('10-13', '10-13'),
        ('13-15', '13-15'),
        ('>15', '>15'),
        ('Unknown', 'Unknown')
    )

    uid = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ownership = models.CharField(
        max_length=255,
        choices=OwnershipChoices,
        default='Unknown',
        blank=False
    )
    access = models.CharField(
        max_length=255,
        choices=accessChoices,
        default='Unknown',
        blank=False
    )
    completion_date = models.DateTimeField(blank=False)
    treatement_type = models.CharField(
        max_length=255,
        choices=treatmentChoices,
        default='Unknown',
        blank=False
    )
    treated_acres = models.IntegerField()
    avg_slope = models.CharField(
        max_length=255,
        choices=slopeChoices,
        default='Unknown',
        blank=False
    )
    status = models.CharField(
        max_length=255,
        choices=statusChoices,
        default='Unknown',
        blank=False
    )
    species = models.CharField(
        max_length=255,
        default='Western Juniper',
        blank=False
    )
    phase = models.CharField(
        max_length=255,
        choices=phaseChoices,
        default='Unknown',
        blank=False
    )
    avg_dbh = models.IntegerField()
    tons_per_acre = models.CharField(
        max_length=255,
        choices=densityChoices,
        default='Unknown',
        blank=False
    )
    latitude = models.DecimalField(
        max_digits=20
        decimal_places=16
    )
    longitude = models.DecimalField(
        max_digits=20
        decimal_places=16
    )
    contact_name = models.CharField(
        max_length=255,
        blank=False
    )
    contact_email = models.EmailField()
    contact_phone = models.CharField(
        max_length=30,
        blank=True
    )
    location = models.PointField(
        srid=settings.GEOMETRY_DB_SRID,
        null=True,
        blank=True,
        default=None
    )
    objects = models.GeoManager()


class ImportEvent(models.Model):

    importStatusChoices = (
        ('complete', 'Complete'),
        ('failed', 'Failed'),
        ('running', 'Running'),
        ('pending', 'Pending'),
        ('unknown', 'Unknown')
    )

    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=255,
        choices=importStatusChoices,
        default='unknown',
        blank=False
    )
    notes = models.TextField()
    user = models.ForeignKey(User)


"""
import
    date	datetime.now()
    status 	[complete, failed, running, pending, unknown]
    notes
    user

treatment_project
    uid
    source
    name
    ownership			[BLM, Private, State, Tribal, USFS, USFWS, Other]
    access				[public, pricate, mixed]
    completion_date		date
    treatment_type		[
                            "Lop and scatter",
                            "Manual thin and pile",
                            "Mechanical thin and pile",
                            "mechanical thin and scatter",
                            "Mechanical thin and yard"
                        ]
    treated_acres		Number (integer)
    avg_slope			[0,10,20,30,40,>40]
    status				["Still standing", "Cut", "Piled"]
    species				Text (["Western juniper"])
    phase				["I", "II", "III"]
    avg_dbh				integer
    tons_per_acre		[1-3, 3-5, 5-7, 7-10, 10-13, 13-15, >15]
    location			Point Geometry
    latitude			Float
    longitude			Float
    contact_name		string
    contact_email		string
    contact_phone		phone number
    expiration			!!!!!!!! TODO !!!!!!

user
    (comes from django core)






"""
