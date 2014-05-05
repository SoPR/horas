from django.conf.urls import patterns, url
from .views import (MeetingUpdateView, MeetingConfirmView,
                    MeetingDetailView, MeetingCancelView)

urlpatterns = patterns(
    '',  # Empty string as prefix

    url('^(?P<pk>\d+)/$', MeetingDetailView.as_view(),
        name='meeting_detail'),

    url('^(?P<pk>\d+)/request/$', MeetingUpdateView.as_view(),
        name='meeting_update'),

    url('^(?P<pk>\d+)/confirm/$', MeetingConfirmView.as_view(),
        name='meeting_confirm'),

    url('^(?P<pk>\d+)/cancel/$', MeetingCancelView.as_view(),
        name='meeting_cancel'),
)
