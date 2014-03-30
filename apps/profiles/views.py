from django.db.models import Q
from django.views.generic import DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from braces.views import LoginRequiredMixin

from .models import User
from ..meetings.models import Meeting
from .forms import ProfileUpdateForm


class ProfileDetailView(DetailView):
    '''
    Displays the user profile information
    '''
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self, *args, **kwargs):
        profile_user = super(ProfileDetailView, self).get_object(*args, **kwargs)
        meetings = Meeting.objects.select_related(
            'mentor', 'protege', 'cancelled_by').filter(Q(mentor=profile_user) | Q(protege=profile_user))

        meetings_available = meetings.filter(state='available', datetime__gt=now())

        meetings_next = meetings.filter(
            state__in=['reserved', 'confirmed'], datetime__gt=now())

        meetings_past = meetings.filter(Q(datetime__lt=now()) |
                                        Q(state__in=['cancelled', 'didnt_happened', 'completed']))

        object = {
            'profile_user': profile_user,
            'meetings': {
                'available': meetings_available,
                'next': meetings_next,
                'past': meetings_past
            }
        }

        return object

    def get_context_data(self, *args, **kwargs):
        ctx = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        ctx['profile_user'] = self.object['profile_user']
        return ctx


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    form_class = ProfileUpdateForm

    def get_queryset(self):
        queryset = super(ProfileUpdateView, self).get_queryset()
        return queryset.filter(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse_lazy('profile_detail', args=[self.object.username])

    def form_valid(self, *args, **kwargs):
        messages.success(self.request, _('Perfil guardado con exito'))
        return super(ProfileUpdateView, self).form_valid(*args, **kwargs)
