from django.conf.urls import patterns, url

from .views import StatsView

urlpatterns = patterns(
    '',  # Empty string as prefix

    url('^$', StatsView.as_view(), name='stats'),

)
