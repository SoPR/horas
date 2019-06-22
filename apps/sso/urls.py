from django.urls import re_path

from . import views

urlpatterns = [re_path("^sso/$", views.single_sign_on, name="single_sign_on")]
