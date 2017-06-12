from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^create_group/$', views.create_group, name='create_group'),
    url(r'^join_group/$', views.join_group, name='join_group'),
]
