from django.conf.urls import patterns, url
from .views import HomePageView

urlpatterns = patterns(
    '',  # Empty string as prefix

    url(r'^$', HomePageView.as_view())
)
