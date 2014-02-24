from django.views.generic.base import TemplateView

from ..profiles.models import User


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        context = super(HomePageView, self).get_context_data()

        context.update({
            'featured_users': User.objects.filter(featured=True),
            'users_count': User.objects.count()
        })

        return context
