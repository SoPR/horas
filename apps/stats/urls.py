from django.conf.urls import url

from .views import StatsView

urlpatterns = [
    url('^$', StatsView.as_view(), name='stats'),
]
