from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url('^$', views.index, name='index'),
    url('^about/$', views.about, name='about'),
)
