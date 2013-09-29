from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^', include('core.urls')),
                       (r'^parse_api/', include('api.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^facebook/', include('django_facebook.urls')),
                       (r'^accounts/', include('django_facebook.auth_urls')),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
)