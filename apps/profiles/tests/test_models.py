# -*- coding: utf-8 -*-
from datetime import time, timedelta
from django.test import TestCase
from django.core.management import call_command
from django.utils.timezone import now

from apps.meetings.models import Meeting
from apps.profiles.models import User


class BaseTestCase(TestCase):
    fixtures = ['apps/profiles/fixtures/dude.json']

    def setUp(self):
        self.dude = User.objects.get(username='dude')
        call_command('create_notice_types')


class UseModelTestCase(BaseTestCase):
    def test_change_settings_creates_meeting(self):
        self.assertEqual(Meeting.objects.all().count(), 0)

        # Change settings and save
        self.dude.day_of_week = 1
        self.dude.save()

        meetings = Meeting.objects.all()
        self.assertEqual(meetings.count(), 1)
        self.assertEqual(meetings[0].mentor, self.dude)
        self.assertEqual(meetings[0].state, 'available')

        # Change settings again and save
        self.dude.start_time = time(1, 0, 0)
        self.dude.save()

        # We should have 2 meetings one of them deleted
        self.assertEqual(Meeting.objects.all().count(), 2)
        self.assertEqual(Meeting.objects.filter(state='deleted').count(), 1)

        # Check that we have only one available
        meetings = Meeting.objects.filter(state='available')
        self.assertEqual(meetings.count(), 1)
        self.assertEqual(meetings[0].mentor, self.dude)

        # Change settings again and save
        self.dude.timezone = 'US/Pacific'
        self.dude.save()

        # We should have 3 meetings 2 of them deleted
        self.assertEqual(Meeting.objects.all().count(), 3)
        self.assertEqual(Meeting.objects.filter(state='deleted').count(), 2)

        # Check that we have only one available
        meetings = Meeting.objects.filter(state='available')
        self.assertEqual(meetings.count(), 1)
        self.assertEqual(meetings[0].mentor, self.dude)

    def test_get_absolute_url(self):
        url = self.dude.get_absolute_url()
        self.assertEqual(url, '/dude/')

    def test_get_url_with_domain(self):
        url = self.dude.get_url_with_domain()
        self.assertEqual(url, 'http://example.com/dude/')

    def test_get_tiny_name(self):
        self.assertEqual(self.dude.get_tiny_name(), 'J. Lebowski')

    def test_has_complete_profile_should_return_true_if_complete(self):
        self.assertTrue(self.dude.has_complete_profile())

    def test_has_complete_profile_false_first_name(self):
        self.dude.first_name = ''
        self.assertFalse(self.dude.has_complete_profile())

    def test_has_complete_profile_false_last_name(self):
        self.dude.last_name = ''
        self.assertFalse(self.dude.has_complete_profile())

    def test_has_complete_profile_false_city(self):
        self.dude.city = ''
        self.assertFalse(self.dude.has_complete_profile())

    def test_has_complete_profile_false_state(self):
        self.dude.state = ''
        self.assertFalse(self.dude.has_complete_profile())

    def test_has_complete_profile_false_bio(self):
        self.dude.bio = ''
        self.assertFalse(self.dude.has_complete_profile())

    def test_has_complete_profile_false_formats(self):
        self.dude.skype = ''
        self.dude.phone = ''
        self.dude.google = ''
        self.dude.jitsi = ''
        self.dude.address = ''
        self.assertFalse(self.dude.has_complete_profile())

    def test_has_complete_profile_true_formats_just_one(self):
        self.dude.skype = 'skypename'
        self.dude.phone = ''
        self.dude.google = ''
        self.dude.jitsi = ''
        self.dude.address = ''
        self.assertTrue(self.dude.has_complete_profile())

        self.dude.skype = ''
        self.dude.phone = '1231231234'
        self.assertTrue(self.dude.has_complete_profile())

        self.dude.phone = ''
        self.dude.google = 'google@example.com'
        self.assertTrue(self.dude.has_complete_profile())

        self.dude.google = ''
        self.dude.jitsi = 'jitsi@example.com'
        self.assertTrue(self.dude.has_complete_profile())

        self.dude.jitsi = ''
        self.dude.address = '123 Main street'
        self.assertTrue(self.dude.has_complete_profile())

    def test_get_location(self):
        self.assertEqual(self.dude.get_location(), 'Los Angeles, California')

    def test_get_all_meeting_formats(self):
        formats = self.dude.get_all_meeting_fromats()

        self.assertEqual(formats[0][0], '123-123-1234')
        self.assertEqual(formats[0][1], 'phone')

        self.assertEqual(formats[1][0], 'thedude')
        self.assertEqual(formats[1][1], 'skype')

        self.assertEqual(formats[2][0], 'thedude@example.com')
        self.assertEqual(formats[2][1], 'google')

        self.assertEqual(formats[3][0], 'thedude@example.com')
        self.assertEqual(formats[3][1], 'jitsi')

        addr = '123 Dude Rd.\r\nLos Angeles, CA\r\n123123'
        self.assertEqual(formats[4][0], addr)
        self.assertEqual(formats[4][1], 'inperson')

    def test_get_meeting_format_information(self):
        phone = self.dude.get_meeting_format_information('phone')
        self.assertEqual(phone, '123-123-1234')

    def test_get_meeting_format_name(self):
        phone_name = self.dude.get_meeting_format_name('phone').encode('utf8')
        self.assertEqual(phone_name, u'Teléfono'.encode('utf8'))

    def test_get_meeting_formats(self):
        formats = self.dude.get_meeting_formats()
        self.assertEqual(len(formats), 5)
        self.assertEqual(type(formats[0]), tuple)
        self.assertEqual(formats[0][0], 'phone')

    def test_get_meeting_formats_string(self):
        expected = u'En persona (Los Angeles, California), '\
                   u'Google, Jitsi, Skype, Teléfono'

        self.assertEqual(
            self.dude.get_meeting_formats_string(), expected.encode('utf8'))

    def test_get_or_create_meeting_should_create_if_no_meetings(self):
        self.assertEqual(Meeting.objects.all().count(), 0)
        self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 1)
        self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 1)

    def test_get_or_create_meeting_states(self):
        self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 1)

        Meeting.objects.filter(state='available').update(state='confirmed')
        self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 1)

        Meeting.objects.filter(state='confirmed').update(state='reserved')
        self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 1)

        Meeting.objects.filter(state='reserved').update(state='cancelled')
        self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 2)

        Meeting.objects.filter(state='available').update(state='deleted')
        self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 3)

        Meeting.objects.filter(state='available').update(state='unused')
        self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 4)

    def test_get_or_create_meeting_dates(self):
        meeting, created = self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 1)

        meeting.datetime = meeting.datetime - timedelta(days=8)
        meeting.save()
        meeting, created = self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 2)

        meeting.datetime = meeting.datetime + timedelta(seconds=1)
        meeting.save()
        meeting, created = self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 2)

        meeting.datetime = meeting.datetime + timedelta(days=8)
        meeting.save()
        meeting, created = self.dude.get_or_create_meeting()
        self.assertEqual(Meeting.objects.all().count(), 3)


