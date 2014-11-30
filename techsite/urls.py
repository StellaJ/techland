from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', 'techsite.views.home'),
    url(r'^home/$', 'techsite.views.home'),
)