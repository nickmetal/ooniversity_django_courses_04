# -*- coding: cp1251 -*-
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from django.views.generic import RedirectView

from . import views
from feedbacks.views import FeedbackView


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('blog:index')),name='index'),
    # url(r'^$',views.index,name='index'),
    url(r'^getdata/$',views.getJSNdata,name='getJSNdata'),
    url(r'^feedback/', FeedbackView.as_view(),name='feedback'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^test/$',views.test,name='test'),
    url(r'^login/$',views.login,name='login'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^student_detail/$',views.student_detail,name='student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
)
