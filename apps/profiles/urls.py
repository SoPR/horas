from django.urls import path

from .feeds import ProfileCalendarFeed
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path("", ProfileDetailView.as_view(), name="profile_detail"),
    path("update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("ical/", ProfileCalendarFeed(), name="profile_calendar_feed"),
]
