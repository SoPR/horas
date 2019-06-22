from django.urls import re_path

from .views import HomePageView

urlpatterns = [re_path(r"^$", HomePageView.as_view(), name="home")]
