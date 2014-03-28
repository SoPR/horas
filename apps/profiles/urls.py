from django.conf.urls import patterns, url
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = patterns(
    '',  # Empty string as prefix

    url(r'^$',
        ProfileDetailView.as_view(),
        name='profile_detail'),

    url(r'^update/$',
        ProfileUpdateView.as_view(),
        name='profile_update'),

    # url('^.(?P<format>ics|rss|atom)$', ProfileDetailView.as_view()),
)
