from django.conf.urls import patterns, url
from .views import MeetingUpdateView

urlpatterns = patterns(
    '',  # Empty string as prefix

    url('^(?P<pk>\d+)/$', MeetingUpdateView.as_view(), name='meeting_detail'),
)
