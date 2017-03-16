from django.conf.urls import url

from . import views

urlpatterns = [
    url('^sso/$', views.single_sign_on, name='single_sign_on'),
]
