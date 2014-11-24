from django.conf.urls import url

from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^services$', views.services, name='services'),
    url(r'^equipment$', views.equipment, name='equipment'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^external$', views.external, name='external'),
    url(r'^join$', views.join, name='join'),
    url(r'^crew$', views.crew, name='crew'),
    url(r'^hots$', views.hots, name='hots'),
    url(r'^alumni$', views.alumni, name='alumni'),
    url(r'^events$', views.events, name='events'),
    url(r'^events70$', views.events70, name='events70'),
    url(r'^events80$', views.events80, name='events80'),
    url(r'^events90$', views.events90, name='events90'),
    url(r'^events00$', views.events00, name='events00'),
    url(r'^timelapse$', views.timelapse, name='timelapse'),
    url(r'^accolades$', views.accolades, name='accolades'),
]
