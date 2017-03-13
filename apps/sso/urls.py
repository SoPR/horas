from django.conf.urls import url

urlpatterns = [
    '',  # Empty string as prefix

    url('^sso/$', 'apps.sso.views.single_sign_on', name='single_sign_on'),

]
