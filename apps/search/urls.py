from django.urls import re_path

from .views import SearchView

urlpatterns = [
    re_path("^$", SearchView.as_view(), name="search_list"),
    # url('^\?q=(?P<query>[-\w]+)', SearchView.as_view(), name='search_query'),
]
