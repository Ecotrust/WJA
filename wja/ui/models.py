from django.db import models

# Create your models here.

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
