from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^signin/$', views.signin, name='signin'),
    path(r'^signup/$', views.signup, name='signup')
]