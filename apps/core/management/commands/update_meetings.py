"""
This command is responsible for updating the state of meetings
based on the defined rules. This rules are partially documented
on apps.meetings.states module.
"""
from django.core.management.base import BaseCommand

from apps.meetings.models import Meeting
from apps.profiles.models import User


class Command(BaseCommand):
    help = "Updates meeting state."

    def handle(self, *args, **kwargs):
        # 1. flag unused meetings
        unused_meetings = Meeting.objects.filter(state=Meeting.STATES.AVAILABLE.value)

        for meeting in unused_meetings:
            if meeting.is_in_past():
                meeting.flag_unused()
                meeting.save()

        # 2. create all missing meetings
        users = User.objects.filter(is_active=True)

        for u in users:
            meeting, created = u.get_or_create_meeting()
