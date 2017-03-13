from django.conf.urls import url
from .views import HomePageView

urlpatterns = [
    '',  # Empty string as prefix

    url(r'^$', HomePageView.as_view(), name='home')
]
