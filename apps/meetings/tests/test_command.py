# -*- coding: utf-8 -*-
from datetime import timedelta
from django.utils.timezone import now

from apps.meetings.tests import MeetingBaseTestCase
from apps.meetings.models import Meeting


class UpdateMeetingsCommandTestCase(MeetingBaseTestCase):
    def test_should_flag_available_in_past_as_unused(self):
        m = Meeting.objects.create(state='available',
            mentor=self.dude, datetime=now() - timedelta(hours=1, seconds=1))

        self.assertEquals(Meeting.objects.filter(state='unused').count(), 0)
        self.assertEquals(Meeting.objects.filter(state='available').count(), 2)

        self.call_command('update_meetings')

        self.assertEquals(Meeting.objects.get(pk=m.id).state, 'unused')
        self.assertEquals(Meeting.objects.filter(state='unused').count(), 1)
        self.assertEquals(Meeting.objects.filter(state='available').count(), 2)

    def test_should_create_missing_meetings(self):
        Meeting.objects.all().delete()
        self.assertEquals(Meeting.objects.filter(state='available').count(), 0)
        self.call_command('update_meetings')
        self.assertEquals(Meeting.objects.filter(state='available').count(), 1)
