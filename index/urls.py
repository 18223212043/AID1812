from django.conf.urls import url
from . import views

#访问路径是：index/
urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^addauthor$',views.addauthor),
    url(r'^queryauthor$', views.queryauthor),
    url(r'^$', views.index),
]