from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.core.cache import cache

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

        featured = cache.get('home:featured')
        if featured is None:
            featured = User.objects.filter(featured=True)
            cache.set('home:featured', featured, 300)

        count = cache.get('home:count')
        if count is None:
            count = getattr(Stat.objects.get_latest('users:all'), 'count', 0)
            cache.set('home:count', count, 300)

        context.update({
            'featured_users': featured,
            'users_count': count
        })

        return context
