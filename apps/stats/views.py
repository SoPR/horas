from django.views.generic import TemplateView
from django.db.models import Count

from apps.profiles.models import User
from .models import Stat

class StatsView(TemplateView):
    template_name = 'stats/stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)

        context['meetings'] = [
            Stat.objects.get_latest('meetings:all'),
            Stat.objects.get_latest('meetings:available'),
            Stat.objects.get_latest('meetings:confirmed'),
            Stat.objects.get_latest('meetings:reserved'),
            Stat.objects.get_latest('meetings:deleted'),
            Stat.objects.get_latest('meetings:didnt_happen'),
            Stat.objects.get_latest('meetings:did_happen'),
            Stat.objects.get_latest('meetings:unused'),
            Stat.objects.get_latest('meetings:waiting_for_reply'),
            Stat.objects.get_latest('meetings:cancelled'),
        ]

        context['users'] = {
            'stats': [
                Stat.objects.get_latest('users:all'),
                Stat.objects.get_latest('users:complete')
            ],
            'recently_joined': User.objects.all().order_by('-date_joined')[:5]
        }

        return context
