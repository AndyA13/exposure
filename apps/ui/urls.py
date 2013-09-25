from django.conf.urls import patterns, url

urlpatterns = patterns('ui.views',
    url(r'^$', 'home'),
    url(r'^(?P<photo_set_slug>[\w-]+)/$', 'photo_set'),
    url(r'^(?P<photo_set_slug>[\w-]+)/(?P<photo_slug>[\w-]+)/$', 'photo_detail'),
)
