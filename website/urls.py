from django.conf.urls import url
from website.views import MarkdownView, JoinView, RequestView

urlpatterns = [
    url(r'^$', MarkdownView.as_view(template_name="index.html", markdown="index.md"), name='index'),
    url(r'^services$', MarkdownView.as_view(markdown="services.md"), name='services'),
    url(r'^equipment$', MarkdownView.as_view(markdown="equipment.md"), name='equipment'),
    url(r'^contact$', MarkdownView.as_view(markdown="contact.md"), name='contact'),
    url(r'^external$', MarkdownView.as_view(markdown="external.md"), name='external'),
    url(r'^join$', JoinView.as_view(), name='join'),
    url(r'^joined$', MarkdownView.as_view(markdown="joined.md"), name='joined'),
    url(r'^crew$', MarkdownView.as_view(markdown="crew.md"), name='crew'),
    url(r'^hots$', MarkdownView.as_view(markdown="hots.md"), name='hots'),
    url(r'^alumni$', MarkdownView.as_view(markdown="alumni.md"), name='alumni'),
    url(r'^events$', MarkdownView.as_view(markdown="events.md"), name='events'),
    url(r'^events70$', MarkdownView.as_view(markdown="events-1970.md"), name='events70'),
    url(r'^events80$', MarkdownView.as_view(markdown="events-1980.md"), name='events80'),
    url(r'^events90$', MarkdownView.as_view(markdown="events-1990.md"), name='events90'),
    url(r'^events00$', MarkdownView.as_view(markdown="events-2000.md"), name='events00'),
    url(r'^timelapse$', MarkdownView.as_view(markdown="timelapse.md"), name='timelapse'),
    url(r'^accolades$', MarkdownView.as_view(markdown='accolades.md'), name='accolades'),
    url(r'^request$', RequestView.as_view(), name='request'),
]
