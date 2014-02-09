from django.conf.urls import patterns, url
from .views import ProfileDetailView

urlpatterns = patterns(
    '',  # Empty string as prefix

    url('^(?P<username>.*)/$', ProfileDetailView.as_view(), name='profile_detail'),
    # url('^$', ProfileDetailView.as_view(), name='profile_detail')
)
