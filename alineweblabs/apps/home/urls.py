from django.conf.urls import patterns, url



urlpatterns = patterns('alineweblabs.apps.home.views',

    url(r'^$','index_view',name='home.view'),

)