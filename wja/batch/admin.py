from django.contrib import admin
from batch.models import *

class BatchAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'user', 'status', 'notes')
    list_filter = ('date_created', 'user', 'status', 'notes')
    ordering = ['date_created', 'user', 'status', 'notes']

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'project_name', 'data_source', 'ownership', 'access', 'treatment_date', 'treatment_type', 'treated_acres', 'average_slope', 'current_status', 'tree_species', 'juniper_phase', 'average_dbh', 'tons_per_acre', 'contact_name', 'contact_email', 'contact_phone')
    list_filter = ('unique_id', 'project_name', 'data_source', 'batch__date_created', 'ownership', 'access', 'treatment_date', 'treatment_type', 'treated_acres', 'average_slope', 'current_status', 'tree_species', 'juniper_phase', 'average_dbh', 'tons_per_acre', 'contact_name', 'contact_email', 'contact_phone')
    ordering = ['unique_id', 'project_name', 'data_source', 'batch__date_created', 'ownership', 'access', 'treatment_date', 'treatment_type', 'treated_acres', 'average_slope', 'current_status', 'tree_species', 'juniper_phase', 'average_dbh', 'tons_per_acre', 'contact_name', 'contact_email', 'contact_phone']

admin.site.register(Batch, BatchAdmin)
admin.site.register(Treatment, TreatmentAdmin)

