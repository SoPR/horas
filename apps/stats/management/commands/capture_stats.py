"""
Get and store stats
"""
from django.core.management.base import BaseCommand
from django.db.models import Count
from django.utils.timezone import now

from apps.meetings.models import Meeting
from apps.profiles.models import User
from apps.stats.models import Stat


class Command(BaseCommand):
    help = 'Gets and saves application stats'

    def handle(self, *args, **kwargs):
        stats = []

        # Meeting
        meetings = Meeting.objects.values(
            'state').order_by().annotate(Count('state'))

        for meeting in meetings:
            stats.append(
                Stat(name='meetings:{0}'.format(meeting['state']),
                     count=meeting['state__count'])
            )

        # Users
        all_users = User.objects.all().order_by('-date_joined')
        stats.append(Stat(name='users:all', count=all_users.count()))
        stats.append(Stat(name='users:complete',
                     count=len([u for u in all_users if u.has_complete_profile()])))

        print('-> CaptureStats', now(), stats)
        Stat.objects.bulk_create(stats)



