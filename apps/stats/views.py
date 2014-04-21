from django.views.generic import TemplateView
from django.db.models import Count

from apps.meetings.models import Meeting
from apps.profiles.models import User

class StatsView(TemplateView):
    template_name = 'stats/stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)

        context['meetings'] = Meeting.objects.values(
                                'state').order_by().annotate(Count('state'))

        all_users = User.objects.all().order_by('-date_joined')
        context['users'] = {
            'all__count': all_users.count(),
            'complete__count': len([u for u in all_users if u.has_complete_profile()]),
            'recently_joined': all_users[:4]
        }

        return context
