from django.conf.urls import patterns, url
from .views import SearchView

urlpatterns = patterns(
    '',  # Empty string as prefix

    url('^$', SearchView.as_view(), name='search_list'),
)
