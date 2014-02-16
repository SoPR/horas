from django.views.generic import DetailView, UpdateView

from braces.views import LoginRequiredMixin

from .models import User


class ProfileDetailView(LoginRequiredMixin, DetailView):
    '''
    Displays the user profile information
    '''
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
