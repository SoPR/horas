# -*- coding: utf-8 -*-
from datetime import timedelta

from django.utils.timezone import now
from django_states.exceptions import PermissionDenied

from apps.meetings.tests import MeetingBaseTestCase
from apps.profiles.models import User


class MeetingStatesTestCase(MeetingBaseTestCase):
    def test_created_meeting_should_be_available(self):
        self.assertEqual(self.meeting.state, 'available')

    def test_available_can_become_reserved_by_other_user(self):
        self.call_command('create_notice_types')
        self.meeting.get_state_info().make_transition('reserve', self.user2)
        self.assertEqual(self.meeting.state, 'reserved')

    def test_available_cant_be_reserved_by_mentor(self):
        with self.assertRaises(PermissionDenied):
            self.meeting.get_state_info().make_transition('reserve', self.dude)

    def test_reserving_a_meeting_should_set_the_protege(self):
        self.call_command('create_notice_types')
        self.meeting.get_state_info().make_transition('reserve', self.user2)
        self.assertEqual(self.meeting.protege, self.user2)

    def test_mentor_can_confirm_meeting(self):
        self.call_command('create_notice_types')
        self.meeting.state = 'reserved'
        self.meeting.protege = self.user2
        self.meeting.save()
        self.meeting.get_state_info().make_transition('confirm', self.dude)

        self.assertEqual(self.meeting.state, 'confirmed')

    def test_user_other_than_mentor_cant_confirm_meeting(self):
        self.meeting.state = 'reserved'
        self.meeting.save()

        with self.assertRaises(PermissionDenied):
            self.meeting.get_state_info().make_transition('confirm',
                                                          self.user2)

    def test_protege_can_cancel_reserved_meeting(self):
        self.call_command('create_notice_types')
        self.meeting.state = 'reserved'
        self.meeting.protege = self.user2
        self.meeting.save()

        self.meeting.get_state_info().make_transition('cancel_reserved',
                                                      self.user2)

        self.assertEqual(self.meeting.cancelled_by, self.user2)

    def test_mentor_can_cancel_reserved_meeting(self):
        self.call_command('create_notice_types')
        self.meeting.state = 'reserved'
        self.meeting.protege = self.user2
        self.meeting.save()

        self.meeting.get_state_info().make_transition('cancel_reserved',
                                                      self.dude)

        self.assertEqual(self.meeting.cancelled_by, self.dude)

    def test_protege_can_cancel_confirmed_meeting(self):
        self.call_command('create_notice_types')
        self.meeting.state = 'confirmed'
        self.meeting.protege = self.user2
        self.meeting.save()

        self.meeting.get_state_info().make_transition('cancel_confirmed',
                                                      self.user2)

        self.assertEqual(self.meeting.cancelled_by, self.user2)

    def test_mentor_can_cancel_confirmed_meeting(self):
        self.call_command('create_notice_types')
        self.meeting.state = 'confirmed'
        self.meeting.protege = self.user2
        self.meeting.save()

        self.meeting.get_state_info().make_transition('cancel_confirmed',
                                                      self.dude)

        self.assertEqual(self.meeting.cancelled_by, self.dude)

    def test_other_user_cant_cancel_reserved_meeting(self):
        self.meeting.state = 'reserved'
        self.meeting.protege = self.user2
        self.meeting.save()

        user3 = User.objects.create_user(username='u3', password='p3',
                                         email='p3@example.com')

        with self.assertRaises(PermissionDenied):
            self.meeting.get_state_info().make_transition('cancel_reserved',
                                                          user3)

    def test_other_user_cant_cancel_confirmed_meeting(self):
        self.meeting.state = 'confirmed'
        self.meeting.protege = self.user2
        self.meeting.save()

        user3 = User.objects.create_user(username='u3', password='p3',
                                         email='p3@example.com')

        with self.assertRaises(PermissionDenied):
            self.meeting.get_state_info().make_transition('cancel_confirmed',
                                                          user3)


class MeetingModelMethodsTestCase(MeetingBaseTestCase):
    def test_get_absolute_url(self):
        url = self.meeting.get_absolute_url()
        self.assertEqual(url, '/es/dude/meetings/1/')

    def test_get_url_with_domain(self):
        url = self.meeting.get_url_with_domain()
        self.assertEqual(url, 'http://example.com/es/dude/meetings/1/')

    def test_cancelled_by_mentor(self):
        self.meeting.protege = self.user2
        self.meeting.cancelled_by = self.dude
        self.meeting.save()

        self.assertTrue(self.meeting.cancelled_by_mentor())
        self.assertFalse(self.meeting.cancelled_by_protege())

    def test_cancelled_by_protege(self):
        self.meeting.protege = self.user2
        self.meeting.cancelled_by = self.user2
        self.meeting.save()

        self.assertTrue(self.meeting.cancelled_by_protege())
        self.assertFalse(self.meeting.cancelled_by_mentor())

    def test_get_end_time(self):
        self.assertTrue(
            self.meeting.get_end_datetime() > self.meeting.datetime)

    def test_is_in_past_false(self):
        self.assertFalse(self.meeting.is_in_past())

    def test_is_in_past_true(self):
        self.meeting.datetime = now() - timedelta(days=1)
        self.assertTrue(self.meeting.is_in_past())

    def test_get_time_range_string(self):
        self.assertEquals(type(self.meeting.get_time_range_string()), str)
        self.assertTrue(len(self.meeting.get_time_range_string()) > 0)
