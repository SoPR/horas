from django.conf.urls import patterns, url
from .views import MeetingDetailView

urlpatterns = patterns(
    '',  # Empty string as prefix

    url('^(?P<pk>\d+)/$', MeetingDetailView.as_view(), name='meeting_detail'),
)
