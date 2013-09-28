from django.conf.urls import patterns, include, url


urlpatterns = patterns('core.views',
                       url(r'^$', 'main', name='core_main'),
)