from django.conf.urls import url

from .views import SearchView

urlpatterns = [
    url('^$', SearchView.as_view(), name='search_list'),
    # url('^\?q=(?P<query>[-\w]+)', SearchView.as_view(), name='search_query'),
]
