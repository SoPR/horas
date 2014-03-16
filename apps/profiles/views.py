from django.views.generic import DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from .models import User
from .forms import ProfileUpdateForm


class ProfileDetailView(DetailView):
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
    form_class = ProfileUpdateForm

    def get_queryset(self):
        queryset = super(ProfileUpdateView, self).get_queryset()
        return queryset.filter(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse_lazy('profile_update', args=[self.object.username])
