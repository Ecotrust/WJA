from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError, HttpResponseForbidden
from django.template import RequestContext, loader
import json
from batch.models import Batch, Treatment
from datetime import date, datetime

# Create your views here.
def mapview(request, template_name='ui/map.html', extra_context={}) :

    template = loader.get_template(template_name)

    context = RequestContext(
        request,{
            # 'site': json.dumps(site.geometry.geojson),
            # 'pits': json.dumps([json.dumps({'pk':x.pk,'name':x.name,'score':x.score,'geometry':x.geometry.geojson}) for x in pits])
        }
    )

    context.update(extra_context)
    return HttpResponse(template.render(context))