from django.core.management.base import BaseCommand

from apps.profiles.models import User


class Command(BaseCommand):
    args = '<user_id user_id ...>'
    help = 'Creates meeting slots for the specified users.'

    def handle(self, *args, **options):
        featured = []

        User.objects.filter(featured=True).update(featured=False)

        users = User.objects.filter(
            is_gravatar_verified=True).exclude(bio='').order_by('?')[:6]

        for user in users:
            user.featured = True
            user.save()

            featured.append(user.username)

        self.stdout.write('{} are now featured'.format(', '.join(featured)))
