from django.shortcuts import render, render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadTreatmentsForm
import datetime
from wja import settings
import xlrd


def handle_imported_treatment_file(f):
    timestamp = datetime.datetime.now().timestamp()
    new_file = '%s/uploaded/treatments_%s.xslx' % (
        settings.MEDIA_ROOT,
        str(timestamp)
    )
    with open(new_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    book = xlrd.open_workbook(new_file)     #Try replacing 'new_file' with 'f' and not saving anything!
    if not book.nsheets == 1:
        import ipdb
        ipdb.set_trace()
    sheet = book.sheet_by_index(0)
    headers = sheet.row_values(0)

    # TODO:
    # save new import event
    # get import id
    # make lookup table for headers and db cols
    # loop through rows (can we get row count?)
    #   cell = sheet.cell(row,column)
    #   treat_obj[headers_lookup[headers[column]]] = cell.value
    # create object of values, including adding import event id
    # save as new Treatment
    # when done, update import status to complete


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
