from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.ship_list),
    url(r'^create/$', views.create_quote),
    url(r'^detail/(?P<id>\d+)/$', views.quote_detail , name='detail'),

    url(r'^detailadd/$', views.quote_create_line),
    url(r'^showcustomer/(?P<id>\d+)/$', views.customer_name),

    url(r'^export_pdf/$', views.export_pdf),

    #url(r'^productdesc/(?P<id>\d+)/$', views.product_desc),
]
