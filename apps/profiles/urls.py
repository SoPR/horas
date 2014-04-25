from django.conf.urls import patterns, url

from .feeds import ProfileCalendarFeed
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = patterns(
    '',  # Empty string as prefix

    url(r'^$',
        ProfileDetailView.as_view(),
        name='profile_detail'),

    url(r'^update/$',
        ProfileUpdateView.as_view(),
        name='profile_update'),

    url(r'^ical/$', ProfileCalendarFeed(), name='profile_calendar_feed'),
)
