from django.views.generic import DetailView, UpdateView
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from .models import User


class ProfileDetailView(DetailView):
    '''
    Displays the user profile information
    '''
    queryset = User.objects.select_related('location', 'location__country')
    slug_field = 'username'
    slug_url_kwarg = 'username'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
