from django.conf.urls import url
from django.contrib import admin
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ProductList.as_view(template_name = '/product/list.html')),
    url(r'^create/$', ProductCreate.as_view() ),
    url(r'^detail/(?P<pk>[0-9]+)/$', ProductDetail.as_view() ),
    url(r'^update/(?P<pk>[0-9]+)/$', ProductUpdate.as_view() ),

]
