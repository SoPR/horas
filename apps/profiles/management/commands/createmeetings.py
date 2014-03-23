"""
This command will create meeting for all active users.

Meeting start_time - To calculate the meeting's start time
we take the time the user choose and apply the user's
timezone of choice.

Then we convert that datetime to the timezone specified
in django's TIME_ZONE setting.
"""

import time
from django.core.management.base import BaseCommand

from ....profiles.models import User

class Command(BaseCommand):
    args = '<user_id user_id ...>'
    help = 'Creates meeting slots for the specified users.'

    def handle(self, *args, **options):
        run_start = time.time()
        meetings_created = []

        if args:
            users = User.objects.filter(pk__in=args, is_active=True)
        else:
            users = User.objects.filter(is_active=True)


        for user in users:
            m, created = user.create_meeting_slot()

            if created:
                meetings_created.append(m)
                meesage = '--> Created meeting for user {0} on {1}'
                self.stdout.write(meesage.format(m.mentor, m.datetime))

        run_time = round(time.time() - run_start)

        if meetings_created > 0:
            message = '--> Succesfully created {0} meetings in {1} secs'
            self.stdout.write(message.format(len(meetings_created), run_time))
        else:
            self.stdout.write('--> No meetings creted, run time {0} secs'.format(run_time))
