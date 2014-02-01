from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',  # Empty string as prefix

    url(r'^admin/', include(admin.site.urls)),
    url(r'^profiles/', include('apps.profiles.urls')),
    url(r'^accounts/', include('allauth.urls')),
)
