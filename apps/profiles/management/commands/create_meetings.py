from django.core.management.base import BaseCommand

from apps.profiles.models import User


class Command(BaseCommand):
    args = '<user_id user_id ...>'
    help = 'Creates meeting slots for the specified users.'

    def handle(self, *args, **options):
        meetings_created = []

        if args:
            users = User.objects.all(pk__in=args)
        else:
            users = User.objects.all()

        for user in users:
            meetings_created.append(user.create_meeting_slot())

        self.stdout.write('Succesfully created {} meetings.'.format(
            len(meetings_created)))
