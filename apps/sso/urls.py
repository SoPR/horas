from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',  # Empty string as prefix

    url('^sso/$', 'apps.sso.views.single_sign_on', name='single_sign_on'),

)
