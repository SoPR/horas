# -*- coding: utf-8 -*-
from datetime import timedelta
from django.utils.timezone import now

from django_states.exceptions import PermissionDenied

from apps.core.tests import BaseTestCase
from apps.meetings.models import Meeting
from apps.profiles.models import User


class MeetingStatesTestCase(BaseTestCase):
    def setUp(self):
        super(MeetingStatesTestCase, self).setUp()

        self.user2 = User.objects.create_user(
            username='user2', password='123', email='user2@example.com')

        self.meeting = Meeting.objects.create(
            mentor=self.dude, datetime=now() + timedelta(days=1))

    def test_created_meeting_should_be_available(self):
        self.assertEqual(self.meeting.state, 'available')

    def test_available_can_become_reserved_by_other_user(self):
        self.meeting.get_state_info().make_transition('reserve', self.user2)
        self.assertEqual(self.meeting.state, 'reserved')

    def test_available_cant_be_reserved_by_mentor(self):
        with self.assertRaises(PermissionDenied):
            self.meeting.get_state_info().make_transition('reserve', self.dude)

    def test_reserving_a_meeting_should_set_the_protege(self):
        self.meeting.get_state_info().make_transition('reserve', self.user2)
        self.assertEqual(self.meeting.protege, self.user2)

    def test_mentor_can_confirm_meeting(self):
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
        self.meeting.state = 'reserved'
        self.meeting.protege = self.user2
        self.meeting.save()

        self.meeting.get_state_info().make_transition('cancel_reserved',
                                                      self.user2)

        self.assertEqual(self.meeting.cancelled_by, self.user2)

    def test_mentor_can_cancel_reserved_meeting(self):
        self.meeting.state = 'reserved'
        self.meeting.protege = self.user2
        self.meeting.save()

        self.meeting.get_state_info().make_transition('cancel_reserved',
                                                      self.dude)

        self.assertEqual(self.meeting.cancelled_by, self.dude)

    def test_protege_can_cancel_confirmed_meeting(self):
        self.meeting.state = 'confirmed'
        self.meeting.protege = self.user2
        self.meeting.save()

        self.meeting.get_state_info().make_transition('cancel_confirmed',
                                                      self.user2)

        self.assertEqual(self.meeting.cancelled_by, self.user2)

    def test_mentor_can_cancel_confirmed_meeting(self):
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



class MeetingModelTestCase(BaseTestCase):
    pass
