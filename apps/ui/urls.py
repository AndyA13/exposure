from django.conf.urls import patterns, url

urlpatterns = patterns('ui.views',
    url(r'^$', 'home', name="home"),
    url(r'^sets/(?P<photo_set_slug>[\w-]+)/$', 'photo_set', name="photo_set"),
    url(r'^sets/(?P<photo_set_slug>[\w-]+)/(?P<photo_slug>[\w-]+)/$', 'photo_detail', name="set_photo_detail"),
    url(r'^photo/(?P<photo_slug>[\w-]+)/$', 'photo_detail', {'photo_set_slug': None}, name="photo_detail"),
)
