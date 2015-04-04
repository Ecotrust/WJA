from django.shortcuts import render, render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadTreatmentsForm
import datetime
from wja import settings
import xlrd
from ui.models import *


def handle_imported_treatment_file(f, user):
    timestamp = datetime.datetime.now().timestamp()
    new_file = '%s/uploaded/treatments_%s.xslx' % (
        settings.MEDIA_ROOT,
        str(timestamp)
    )
    with open(new_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    import_event = ImportEvent(status='running', user=user)
    import_event.save()
    book = xlrd.open_workbook(new_file)
    datemode = book.datemode
    sheet = book.sheet_by_index(0)
    headers = sheet.row_values(0)
    labels = [x.value for x in sheet.row(0)]
    id_index = labels.index(settings.HEADER_REVERSE_LOOKUP['unique_id'])
    rowcount = sheet.nrows
    saved_count = 0

    for rownum in range(1, rowcount):
        if not sheet.cell(rownum, id_index).ctype == 2:
            num_rows = rownum-2
            print('Blank row found: row %s' % str(rownum))
            break
        cell_id = sheet.cell(rownum, id_index).value
        treatment, created = TreatmentProject.objects.get_or_create(
            unique_id=cell_id
        )
        print('Treatment with ID %s created' % str(cell_id))
        for colnum, header in enumerate(headers):
            if colnum != id_index:
                cell = sheet.cell(rownum, colnum)
                if cell.ctype == 3:
                    xldate = cell.value
                    time_tuple = xlrd.xldate_as_tuple(xldate, datemode)
                    value = datetime.datetime(*time_tuple)
                else:
                    value = cell.value
                setattr(
                    treatment,
                    settings.HEADER_LOOKUP[header],
                    value
                )
                print('Treatment field %s updated with value %s' % (
                    settings.HEADER_LOOKUP[header],
                    str(value)
                ))
        try:
            treatment.save()
        except TypeError:
            import ipdb
            ipdb.set_trace()
        saved_count += 1
        print('Treatment %s saved. %s total treatments saved' % (
            str(cell_id),
            str(saved_count)
        ))

    if saved_count != num_rows:
        print('Saved: %s' % str(saved_count))
        print('Rows imported" %s' % str(num_rows))
        import ipdb
        ipdb.set_trace()

    setattr(import_event, status, 'complete')
    import_event.save()

    # TODO:
    # save new import event
    # get import id
    # make lookup table for headers and db cols
    # loop through rows (can we get row count?)
    #   cell = sheet.cell(row,column)
    #   treat_obj[settings.HEADER_LOOKUP[headers[column]]] = cell.value
    # create object of values, including adding import event id
    # save as new Treatment
    # when done, update import status to complete
    # REMOVE NEW XL FILE (and any others, too!)


def import_admin(
    request,
    template_name='admin/admin_utils/import_admin.html',
    extra_context={}
):
    if request.method == 'POST':
        form = UploadTreatmentsForm(request.POST, request.FILES)
        if form.is_valid():
            handle_imported_treatment_file(request.FILES['file'], request.user)
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
