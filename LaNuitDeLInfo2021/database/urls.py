from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^drop/$', views.drop, name='drop'),
    url(r'^ssearch/$', views.search_ship, name='search')
]