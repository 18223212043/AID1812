from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^show/$',views.show),
    url(r'^template/$',views.template),
    #当访问路径是空的时候
    url(r'^$',views.index)
]