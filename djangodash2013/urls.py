from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^', include('core.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^facebook/', include('django_facebook.urls')),
                       (r'^accounts/', include('django_facebook.auth_urls')),
)
