from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.dps_list),
    url(r'^create/$', views.dps_create),
    url(r'^detail/(?P<id>\d+)/$', views.dps_detail , name='detail'),
    url(r'^update/(?P<id>\d+)/$', views.dps_update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.dps_delete),
    #url(r'^customertitle/(?P<id>\d+)/$', views.customer_name),
    #url(r'^productdesc/(?P<id>\d+)/$', views.product_desc),
]
