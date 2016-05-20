# encoding: utf-8

from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.PostListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
)
