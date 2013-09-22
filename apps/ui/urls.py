from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'ui.views.home'),
    url(r'^set/$', 'ui.views.photoset'),
    url(r'^photo/$', 'ui.views.photo')
)
