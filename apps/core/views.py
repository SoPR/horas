from django.core.cache import cache
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

from ..profiles.models import User
from ..stats.models import Stat


class HomePageView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('search_list'))

        return super(HomePageView, self).dispatch(*args, **kwargs)

    def get_context_data(self):
        context = super(HomePageView, self).get_context_data()

        featured_section = cache.get('home:featured:section')
        if featured_section is None:
            featured_section = {
                'featured_users': User.objects.filter(featured=True),
                'users_count': getattr(Stat.objects.get_latest('users:all'), 'count', 0)
            }
            cache.set('home:featured:section', featured_section, 300)

        context.update(featured_section)
        return context
