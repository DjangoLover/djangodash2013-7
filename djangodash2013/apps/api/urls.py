from django.conf.urls import patterns, include, url


urlpatterns = patterns('api.views',
                       url(r'^famous', 'get_famous', name='get_famous'),
                       url(r'^events', 'get_events', name='get_events'),
)