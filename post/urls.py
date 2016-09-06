from django.conf.urls import url
from django.contrib import admin

from .views import PostList, PostDetail, PostCreate, PostUpdate


urlpatterns = [
    url(r'^$', PostList.as_view(template_name = 'post_list.html')),
    url(r'^create/$', PostCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', PostDetail.as_view(), name='detail' ),
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdate.as_view()  , name='post-update'),


]
