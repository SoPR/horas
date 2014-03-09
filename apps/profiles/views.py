from django.views.generic import DetailView, UpdateView
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from .models import User


class ProfileDetailView(LoginRequiredMixin, DetailView):
    '''
    Displays the user profile information
    '''
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get(self, request, *args, **kwargs):
        username = self.kwargs.get(self.slug_url_kwarg).lower()

        if username == 'me':
            return redirect('profile_detail', username=request.user.username)

        return super(ProfileDetailView, self).get(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
