from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('website.urls', namespace="website")),
    url(r'^markdown/', include('django_markdown.urls')),
]
