from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext, loader
from django.http import HttpResponse


def import_admin(
    request,
    template_name='admin/admin_utils/import_admin.html',
    extra_context={}
):
    template = loader.get_template(template_name)
    context = RequestContext(
        request, {}
    )

    context.update(extra_context)
    return HttpResponse(template.render(context))

import_admin = staff_member_required(import_admin)
