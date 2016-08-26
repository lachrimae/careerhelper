from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
#    url(r'^src/', name='app-source'),
    url(r'^test/$', views.test, name='testhome'),
]
