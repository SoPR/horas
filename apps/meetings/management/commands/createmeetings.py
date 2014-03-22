"""
This command will create meeting for all active users.

Meeting start_time - To calculate the meeting's start time
we take the time the user choose and apply the user's
timezone of choice.

Then we convert that datetime to the timezone specified
in django's TIME_ZONE setting.
"""

import pytz
import time
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.timezone import now, make_aware, get_default_timezone

from ....profiles.models import User
from ...models import Meeting
from ...utils import next_weekday

class Command(BaseCommand):

    def handle(self, *args, **options):
        run_start = time.time()
        meetings_created = 0
        users = User.objects.filter(is_active=True)

        for user in users:
            tz = pytz.timezone(user.timezone)
            if user.day_of_week:
                date = next_weekday(now(), user.day_of_week)

                local_time = make_aware(datetime.combine(date, user.start_time), tz)
                tz_datetime = local_time.astimezone(get_default_timezone())

                m, created = Meeting.objects.get_or_create(mentor=user, datetime=tz_datetime)

                if created:
                    meetings_created += 1
                    self.stdout.write(
                        '--> Created meeting for user {0} at {1}'.format(m.mentor, m.datetime))


        run_time = round(time.time() - run_start)
        if meetings_created > 0:
            self.stdout.write(
                '--> Created meetings for {0} users in {1} secs'.format(meetings_created, run_time))
        else:
            self.stdout.write('--> No meetings creted, run time {0} secs'.format(run_time))
