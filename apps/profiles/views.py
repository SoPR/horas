from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, UpdateView

from ..meetings.models import Meeting
from .forms import ProfileUpdateForm
from .models import User


class ProfileDetailView(DetailView):
    """
    Displays the user profile information
    """

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_object(self, *args, **kwargs):
        profile_user = super().get_object(*args, **kwargs)
        meetings = (
            Meeting.objects.select_related("mentor", "protege", "cancelled_by")
            .filter(Q(mentor=profile_user) | Q(protege=profile_user))
            .exclude(state=Meeting.STATES.DELETED.value)
        )

        meetings_available = meetings.filter(
            state=Meeting.STATES.AVAILABLE.value, datetime__gt=now()
        )

        meetings_next = meetings.filter(
            state__in=[Meeting.STATES.RESERVED.value, Meeting.STATES.CONFIRMED.value],
            datetime__gt=now(),
        )

        meetings_past = meetings.filter(
            Q(datetime__lt=now())
            | Q(state__in=[Meeting.STATES.CANCELLED.value, Meeting.STATES.UNUSED.value])
        )

        response_object = {
            "profile_user": profile_user,
            "meetings": {
                "available": meetings_available,
                "next": meetings_next,
                "past": meetings_past,
            },
        }

        return response_object

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["profile_user"] = self.object["profile_user"]
        return ctx


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    form_class = ProfileUpdateForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse_lazy("profile_detail", args=[self.object.username])

    def form_valid(self, *args, **kwargs):
        messages.success(self.request, _("Perfil guardado exitosamente."))
        return super().form_valid(*args, **kwargs)
