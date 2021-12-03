from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^drop/$', views.drop, name='drop'),
    url(r'^ssearch/$', views.search_ship, name='search_ship'),
    url(r'^sdetail(?P<ship_id>[0-9]+)/$', views.ship_detail, name='sdetail'),
    url(r'')
]