from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='app'),
    url(r'^test/$', views.test, name='testhome')
]
