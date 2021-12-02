from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^drop/$', views.drop, name='drop'),
]