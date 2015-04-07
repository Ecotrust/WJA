from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'wja.views.home', name='home'),
    url(r'^admin/import/$', 'admin_utils.views.import_admin'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^treatment/(?P<treatment_id>[0-9]+)', 'ui.views.treatmentview'),
    url(r'^$', 'ui.views.mapview'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
