from django.views.generic import DetailView

from braces.views import LoginRequiredMixin

from .models import User


class ProfileDetailView(LoginRequiredMixin, DetailView):
    '''
    Displays the user profile information
    '''
    model = User

    def get_object(self):
        # Get the currently logged in user
        return self.request.user
