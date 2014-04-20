from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from ..profiles.models import User


class HomePageView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('search_list'))

        return super(HomePageView, self).dispatch(*args, **kwargs)

    def get_context_data(self):
        context = super(HomePageView, self).get_context_data()

        context.update({
            'featured_users': User.objects.filter(featured=True),
            'users_count': User.objects.count()
        })

        return context
