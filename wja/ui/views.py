from django.shortcuts import render
from django.http import HttpResponse
# HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError,
# HttpResponseForbidden
from django.template import RequestContext, loader
import json
from ui.models import ImportEvent, TreatmentProject
from datetime import date, datetime


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
