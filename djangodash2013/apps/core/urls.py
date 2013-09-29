from django.conf.urls import patterns, include, url


urlpatterns = patterns('core.views',
                       url(r'^$', 'main', name='core_main'),
                       url(r'is_mosaic_ready/$', 'is_mosaic_ready', name='core_is_mosaic_ready'),
)