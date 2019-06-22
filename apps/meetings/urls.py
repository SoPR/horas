from django.urls import re_path

from .views import (
    MeetingCancelView,
    MeetingCommentView,
    MeetingConfirmView,
    MeetingDetailView,
    MeetingUpdateView,
)

urlpatterns = [
    re_path(r"^(?P<pk>\d+)/$", MeetingDetailView.as_view(), name="meeting_detail"),
    re_path(
        r"^(?P<pk>\d+)/request/$", MeetingUpdateView.as_view(), name="meeting_update"
    ),
    re_path(
        r"^(?P<pk>\d+)/confirm/$", MeetingConfirmView.as_view(), name="meeting_confirm"
    ),
    re_path(
        r"^(?P<pk>\d+)/cancel/$", MeetingCancelView.as_view(), name="meeting_cancel"
    ),
    re_path(
        r"^(?P<pk>\d+)/comment/$", MeetingCommentView.as_view(), name="meeting_comment"
    ),
]
