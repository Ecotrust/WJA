from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

status_choices = (
    ('Successful', 'Successful'),
    ('Failed', 'Failed')
)

class Batch(models.Model):
    notes = models.TextField(default='', blank=True)
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=status_choices, max_length=255, blank=True, null=True, default='Failed')

    def __str__(self):
        return "Import by {} on {}: {}.".format(
            self.user.username, 
            self.date_created,
            self.status
        )

### For now it will be easier to allow anything that comes in via CSV
    # ownership_choices = (
    #     ('BLM', 'BLM'),
    #     ('Private', 'Private'),
    #     ('State', 'State'),
    #     ('Tribal', 'Tribal'),
    #     ('USFS', 'USFS'),
    #     ('USFWS', 'USFWS'),
    #     ('Other', 'Other')
    # )

    # access_choices = (
    #     ('Public', 'Public'),
    #     ('Private', 'Private'),
    #     ('Mixed', 'Mixed'),
    #     ('Other', 'Other')
    # )

    # treatment_type_choices = (
    #     ('Lop and scatter', 'Lop and scatter'),
    #     ('Manual thin and pile', 'Manual thin and pile'),
    #     ('Mechanical thin and pile', 'Mechanical thin and pile'),
    #     ('Mechanical thin and scatter', 'Mechanical thin and scatter'),
    #     ('Mechanical thin and yard', 'Mechanical thin and yard'),
    #     ('Other', 'Other')
    # )

    # average_slope_choices = (
    #     ('0', '0'),
    #     ('10', '10'),
    #     ('20', '20'),
    #     ('30', '30'),
    #     ('40', '40'),
    #     ('>40', '>40'),
    #     ('Other', 'Other')
    # )

    # current_status_choices = (
    #     ('Still standing', 'Still standing'),
    #     ('Cut', 'Cut'),
    #     ('Piled', 'Piled'),
    #     ('Other', 'Other')
    # )

    # tree_species_choices = (
    #     ('western juniper', 'western juniper'),
    #     ('other', 'other')
    # )

    # juniper_phase_choices = (
    #     ('I', 'I'),
    #     ('II', 'II'),
    #     ('III', 'III'),
    #     ('Other', 'Other')
    # )

    # tons_per_acre_choices = (
    #     ('1-3', '1-3'),
    #     ('3-5', '3-5'),
    #     ('5-7', '5-7'),
    #     ('7-10', '7-10'),
    #     ('10-13', '10-13'),
    #     ('13-15', '13-15'),
    #     ('>15', '>15'),
    #     ('Other', 'Other')
    # )

class Treatment(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    batch = models.ForeignKey(Batch, blank=True, null=True, default=None)
    data_source = models.CharField(max_length=255, blank=True, null=True, default=None)
    project_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    ownership = models.CharField(max_length=255, blank=True, null=True, default=None)
    access = models.CharField(max_length=255, blank=True, null=True, default=None)
    treatment_date = models.DateField(auto_now=False, blank=True, null=True, default=None)
    treatment_type = models.CharField(max_length=255, blank=True, null=True, default=None)
    treated_acres = models.FloatField(blank=True, null=True, default=None)
    average_slope = models.CharField(max_length=255, blank=True, null=True, default=None)
    #Check on this one
    current_status = models.CharField(max_length=255, blank=True, null=True, default=None)
    tree_species = models.CharField(max_length=255, blank=True, null=True, default=None)
    juniper_phase = models.CharField(max_length=255, blank=True, null=True, default=None)
    average_dbh = models.IntegerField(blank=True, null=True, default=None)
    tons_per_acre = models.CharField(max_length=255, blank=True, null=True, default=None)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    geometry = models.PointField(srid=settings.SERVER_SRID, null=True, blank=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    contact_email = models.CharField(max_length=255, blank=True, null=True, default=None)
    contact_phone = models.CharField(max_length=255, blank=True, null=True, default=None)

    def __str__(self):
        return "{}: `{}`".format(self.project_name, self.treatment_date)
