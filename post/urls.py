from django.conf.urls import url
from django.contrib import admin

from .views import PostList, PostDetail


urlpatterns = [
    url(r'^$', PostList.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/$', PostDetail.as_view() ),
]
