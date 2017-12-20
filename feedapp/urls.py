from django.conf.urls import url
from feedapp import views


urlpatterns = [
    # feedapp/blahblahblahh/
    url(r'^1', views.first, name='port1'),
    url(r'^2', views.second, name='port2'),
    url(r'^3', views.third, name='port3'),
    url(r'^4', views.forth, name='port4'),
    # url(r'^success/$', views.success, name='success'),
]