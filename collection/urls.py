from django.conf.urls import url

from . import views

app_name = 'collection'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/$', views.all, name='all'),
]
