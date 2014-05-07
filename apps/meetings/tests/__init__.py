# -*- coding: utf-8 -*-
from datetime import timedelta
from django.utils.timezone import now

from apps.core.tests import BaseTestCase
from apps.meetings.models import Meeting
from apps.profiles.models import User

class MeetingBaseTestCase(BaseTestCase):
    def setUp(self):
        super(MeetingBaseTestCase, self).setUp()

        self.user2 = User.objects.create_user(
            username='user2', password='123', email='user2@example.com')

        self.meeting = Meeting.objects.create(
            mentor=self.dude, datetime=now() + timedelta(days=1))
