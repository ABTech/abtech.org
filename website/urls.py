"""Django View Classes for abtech.org."""

from django.conf.urls import url
from django.views.generic import TemplateView
from website.views import MarkdownView, JoinView, RequestView

urlpatterns = [
    url(r'^$', MarkdownView.as_view(template_name="index.html", markdown="index.md"), name='index'),
    url(r'^services$', MarkdownView.as_view(markdown="services.md"), name='services'),
    url(r'^equipment$', MarkdownView.as_view(markdown="equipment.md"), name='equipment'),
    url(r'^external$', MarkdownView.as_view(markdown="external.md"), name='external'),
    url(r'^join$', JoinView.as_view(), name='join'),
    url(r'^joined$', MarkdownView.as_view(markdown="joined.md"), name='joined'),
    url(r'^crew$', MarkdownView.as_view(markdown="crew.md"), name='crew'),
    url(r'^hots$', MarkdownView.as_view(markdown="hots.md"), name='hots'),
    url(r'^alumni$', MarkdownView.as_view(markdown="alumni.md"), name='alumni'),
    url(r'^events$', MarkdownView.as_view(markdown="events.md"), name='events'),
    url(r'^archives$', MarkdownView.as_view(markdown="archives.md"), name='archives'),
    url(r'^archives70$', MarkdownView.as_view(markdown="archives-1970.md"), name='archives70'),
    url(r'^archives80$', MarkdownView.as_view(markdown="archives-1980.md"), name='archives80'),
    url(r'^archives90$', MarkdownView.as_view(markdown="archives-1990.md"), name='archives90'),
    url(r'^archives00$', MarkdownView.as_view(markdown="archives-2000.md"), name='archives00'),
    url(r'^timelapse$', MarkdownView.as_view(markdown="timelapse.md"), name='timelapse'),
    url(r'^accolades$', MarkdownView.as_view(markdown='accolades.md'), name='accolades'),
    url(r'^request$', RequestView.as_view(), name='request'),
    url(r'^404test$', TemplateView.as_view(template_name="404.html")),
]
