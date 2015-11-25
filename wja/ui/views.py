from django.shortcuts import render
from django.http import HttpResponse
# HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError,
# HttpResponseForbidden
from django.template import RequestContext, loader
import json
from ui.models import ImportEvent, TreatmentProject
from datetime import date, datetime
from collections import OrderedDict


# Create your views here.
def mapview(request, template_name='ui/map.html', extra_context={}):

    template = loader.get_template(template_name)

    imports = [x.to_dict() for x in ImportEvent.objects.all()]
    treatments = [x.to_dict() for x in TreatmentProject.objects.all()]

    context = RequestContext(
        request,
        {
            'sites': json.dumps(treatments),
            'imports': json.dumps(imports)
        }
    )

    context.update(extra_context)
    return HttpResponse(template.render(context))


def treatmentview(
    request,
    treatment_id,
    template_name='ui/treatment.html',
    extra_context={}
):
    template = loader.get_template(template_name)

    treatments = TreatmentProject.objects.filter(unique_id=treatment_id)

    if not len(treatments) == 1:
        treatment = {'unique_id': treatment_id}
        found = False
    else:
        treatment = treatments[0].to_dict()

        #order_treatment is the explicit, defined order of the treatment dictionary
        #every treatment key/value pairs defined in the model are not listed here
        order_treatment = OrderedDict()
        order_treatment['name'] = treatment['name']
        order_treatment['id'] = treatment['id']
        order_treatment['Date'] = treatment['date']
        order_treatment['Ownership'] = treatment['ownership']
        order_treatment['Access'] = treatment['access']
        order_treatment['Latitude'] = treatment['latitude']
        order_treatment['Longitude'] = treatment['longitude']
        order_treatment['Current Status'] = treatment['current_status']
        order_treatment['Contact Name'] = treatment['contact_name']
        order_treatment['Contact Phone'] = treatment['contact_phone']
        order_treatment['Contact Email'] = treatment['contact_email']
        order_treatment['Treatment Type'] = treatment['treatment_type']
        order_treatment['Treated Acres'] = treatment['treated_acres']
        order_treatment['Tree Species'] = treatment['tree_species']
        order_treatment['Juniper Phase'] = treatment['juniper_phase']
        order_treatment['Average Diameter at Breast Height'] = treatment['average_dbh']
        order_treatment['Contact Email'] = treatment['contact_email']
        order_treatment['Tons per Acre'] = treatment['tons_per_acre']
        order_treatment['Average Slope'] = treatment['average_slope']
        order_treatment['Source'] = treatment['source']

        treatment = order_treatment

        found = True

    context = RequestContext(
        request,
        {
            'treatment': treatment,
            'found': found
        }
    )

    context.update(extra_context)
    return HttpResponse(template.render(context))
