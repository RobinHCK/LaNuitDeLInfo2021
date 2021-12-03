from django.conf.urls import url

from . import views

urlpatterns = [
    url('drop/', views.image_upload_view, name='drop'),
    url(r'^ssearch/$', views.search_ship, name='ssearch'),
    url(r'^sdetail(?P<ship_id>[0-9]+)/$', views.detail_ship, name='sdetail'),
    url(r'^psearch/$', views.search_person, name='psearch'),
    url(r'^pdetail(?P<person_id>[0-9]+)/$', views.person_detail, name='pdetail'),
]