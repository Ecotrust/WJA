from django.shortcuts import render, render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadTreatmentsForm
import datetime
from wja import settings


def handle_imported_treatment_file(f):
    timestamp = datetime.datetime.now().timestamp()
    with open(
        '%s/uploaded/treatments_%s.xslx' % (
            settings.MEDIA_ROOT,
            str(timestamp)
        ),
        'wb+'
    ) as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def import_admin(
    request,
    template_name='admin/admin_utils/import_admin.html',
    extra_context={}
):
    if request.method == 'POST':
        form = UploadTreatmentsForm(request.POST, request.FILES)
        if form.is_valid():
            handle_imported_treatment_file(request.FILES['file'])
            return HttpResponseRedirect('/admin/ui/')    # success url
    else:
        form = UploadTreatmentsForm()
    # return render_to_response(template_name, {'form': form})
    template = loader.get_template(template_name)
    context = RequestContext(
        request, {
            'form': form
        }
    )

    context.update(extra_context)
    return HttpResponse(template.render(context))

import_admin = staff_member_required(import_admin)
