from django.conf.urls import patterns, url

from hello import views

urlpatterns = patterns('',
    # ex: /hello/
    url(r'^$', views.index, name='index'),
)

