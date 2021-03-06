from django.core.management import call_command
from django.test import TestCase

from apps.profiles.models import User


class BaseTestCase(TestCase):
    fixtures = ["apps/profiles/fixtures/dude.json"]

    def setUp(self):
        self.dude = User.objects.get(username="dude")
        self.call_command = call_command

    def _login_user(self):
        credentials = {"login": "dude", "password": "thedude"}
        return self.client.post("/es/accounts/login/", credentials)
