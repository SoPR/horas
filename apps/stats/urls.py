from django.urls import re_path

from .views import StatsView

urlpatterns = [re_path("^$", StatsView.as_view(), name="stats")]
