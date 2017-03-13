from django.conf.urls import url

from .views import StatsView

urlpatterns = [
    '',  # Empty string as prefix

    url('^$', StatsView.as_view(), name='stats'),

]
