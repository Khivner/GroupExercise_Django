from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^new_post/$', views.new_post, name='new_post'),
]
