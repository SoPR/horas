from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',  # Empty string as prefix

    url(r'^admin/', include(admin.site.urls)),

    url(r'^search/', include('apps.search.urls')),

    url(r'^meetings/', include('apps.meetings.urls')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^api/v1/', include('apps.sso.urls')),

    # This pages are in apps/core/templates
    url(r'^legal/$', TemplateView.as_view(
        template_name='legal.html'), name='legal'),
    url(r'^about/$', TemplateView.as_view(
        template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(
        template_name='contact.html'), name='contact'),

    url(r'', include('apps.profiles.urls')),

    url(r'^$', include('apps.core.urls')),
)
