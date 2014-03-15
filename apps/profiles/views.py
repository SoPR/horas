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

    def get(self, request, *args, **kwargs):
        user = request.user
        username = self.kwargs.get(self.slug_url_kwarg)

        if user.is_authenticated() and not username:
            return redirect('profile_detail', username=user.username)
        elif not user.is_authenticated() and not username:
            return redirect_to_login(reverse('profile_detail_me'))

        return super(ProfileDetailView, self).get(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
