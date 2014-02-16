from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',  # Empty string as prefix

    url(r'^admin/', include(admin.site.urls)),

    url(r'^search/', include('apps.search.urls')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^(?P<username>[-\w]+)', include('apps.profiles.urls')),

    url(r'^$', include('apps.core.urls')),
)
