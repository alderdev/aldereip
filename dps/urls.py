from django.conf.urls import url
from django.contrib import admin


from .views import WorkorderList, WorkorderDetail, WorkorderCreate


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', WorkorderList.as_view( template_name = 'workorder_list.html' )),
    url(r'^create/$', WorkorderCreate.as_view() ),
    url(r'^detail/(?P<pk>[0-9]+)/$', WorkorderDetail.as_view() ),
    #url(r'^update/(?P<id>\d+)/$', views.dps_update, name='update'),
    #url(r'^delete/(?P<id>\d+)/$', views.dps_delete),
    #url(r'^customertitle/(?P<id>\d+)/$', views.customer_name),
    #url(r'^productdesc/(?P<id>\d+)/$', views.product_desc),
]
