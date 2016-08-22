from django.conf.urls import url
from django.contrib import admin

from .views import PostList, PostDetail, PostCreate, PostUpdate


urlpatterns = [
    url(r'^$', PostList.as_view(template_name = 'post_list.html')),
    url(r'^create/$', PostCreate.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/$', PostDetail.as_view() , name='post-detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', PostUpdate.as_view()  , name='post-update'),


]
