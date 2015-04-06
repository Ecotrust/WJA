from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.gis.geos import Point
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from pytz import timezone
import pytz


class ImportEvent(models.Model):

    importStatusChoices = (
        ('complete', 'Complete'),
        ('failed', 'Failed'),
        ('running', 'Running'),
        ('pending', 'Pending'),
        ('unknown', 'Unknown')
    )

    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=255,
        choices=importStatusChoices,
        default='unknown',
        blank=False
    )
    notes = models.TextField(null=True, blank=True, default=None)
    user = models.ForeignKey(User)

    def to_dict(self):
        datetz = self.date_created.replace(tzinfo=datetime.timezone.utc)
        localdatetz = datetz.astimezone(tz=None)
        date_string = localdatetz.strftime("%I:%M %p %b %d, %Y %Z")
        return {
            'user': str(self.user),
            'date_created': date_string,
            'status': str(self.status),
            'notes': str(self.notes),
        }


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

    unique_id = models.IntegerField(primary_key=True)
    data_source = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    ownership = models.CharField(
        max_length=255,
        choices=ownershipChoices,
        default='Unknown',
        blank=False
    )
    access = models.CharField(
        max_length=255,
        choices=accessChoices,
        default='Unknown',
        blank=False
    )
    treatment_date = models.DateTimeField(
        blank=True,
        null=True,
        default=None
    )
    treatment_type = models.CharField(
        max_length=255,
        choices=treatmentChoices,
        default='Unknown',
        blank=False
    )
    treated_acres = models.IntegerField(
        blank=True,
        null=True,
        default=None
    )
    average_slope = models.CharField(
        max_length=255,
        choices=slopeChoices,
        default='Unknown',
        blank=False
    )
    current_status = models.CharField(
        max_length=255,
        choices=statusChoices,
        default='Unknown',
        blank=False
    )
    tree_species = models.CharField(
        max_length=255,
        default='Western Juniper',
        blank=False
    )
    juniper_phase = models.CharField(
        max_length=255,
        choices=phaseChoices,
        default='Unknown',
        blank=False
    )
    average_dbh = models.IntegerField(
        blank=True,
        null=True,
        default=None
    )
    tons_per_acre = models.CharField(
        max_length=255,
        choices=densityChoices,
        default='Unknown',
        blank=False
    )
    latitude = models.DecimalField(
        max_digits=20,
        decimal_places=16,
        blank=True,
        null=True,
        default=None
    )
    longitude = models.DecimalField(
        max_digits=20,
        decimal_places=16,
        blank=True,
        null=True,
        default=None
    )
    contact_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=None
    )
    contact_email = models.EmailField(
        blank=True,
        null=True,
        default=None
    )
    contact_phone = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default=None
    )
    location = models.PointField(
        srid=settings.GEOMETRY_DB_SRID,
        null=True,
        blank=True,
        default=None
    )
    objects = models.GeoManager()
    batch = models.ForeignKey(ImportEvent)

    def to_dict(self):
        if self.treatment_date is not None:
            datetz = self.treatment_date.replace(tzinfo=datetime.timezone.utc)
            localdatetz = datetz.astimezone(tz=None)
            date_string = localdatetz.strftime("%I:%M %p %b %d, %Y %Z")
        else:
            date_string = ''
        if self.location is not None:
            point = self.location.geojson
        else:
            point = None

        return {
            'id': self.unique_id,
            'source': self.data_source,
            'name': self.project_name,
            'ownership': self.ownership,
            'access': self.access,
            'date': date_string,
            'treatment_type': self.treatment_type,
            'treated_acres': self.treated_acres,
            'average_slope': self.average_slope,
            'current_status': self.current_status,
            'tree_species': self.tree_species,
            'juniper_phase': self.juniper_phase,
            'average_dbh': self.average_dbh,
            'tons_per_acre': self.tons_per_acre,
            'latitude': str(self.latitude),
            'longitude': str(self.longitude),
            'contact_name': self.contact_name,
            'contact_email': self.contact_email,
            'contact_phone': self.contact_phone,
            'batch': self.batch.to_dict(),
            'point': point
        }

    def __str__(self):
        return "{}: `{}`".format(self.project_name, self.treatment_date)


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
