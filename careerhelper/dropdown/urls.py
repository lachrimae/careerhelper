from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$([0-9]{2})-([0-9]{4})/$', views.json, name='dropdown_json'),
    url(r'$majorgroups/$', views.majorgroups, name='dropdown_majorgroups')
]
