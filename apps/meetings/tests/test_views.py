# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from apps.meetings.tests import MeetingBaseTestCase
from apps.comments.models import Comment


class MeetingDetailViewTestCase(MeetingBaseTestCase):
    def test_meeting_should_be_under_the_username_of_the_mentor(self):
        response = self.client.get('/dude/meetings/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name,
                         ['meetings/meeting_detail.html'])

    def test_available_meeting(self):
        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, u'Reunión disponible', status_code=200)
        self.assertContains(response, 'Reservar', status_code=200)

    def test_reserved_meeting(self):
        self.meeting.state = 'reserved'
        self.meeting.protege = self.user2
        self.meeting.save()

        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, u'Reunión reservada', status_code=200)
        self.assertContains(response, 'icon-warning', status_code=200)

    def test_confirmed_meeting(self):
        self.meeting.state = 'confirmed'
        self.meeting.protege = self.user2
        self.meeting.save()

        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, u'Reunión confirmada', status_code=200)
        self.assertContains(response, 'icon-success', status_code=200)

    def test_cancelled_meeting(self):
        self.meeting.state = 'cancelled'
        self.meeting.protege = self.user2
        self.meeting.save()

        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, u'Reunión cancelada', status_code=200)
        self.assertContains(response, 'icon-cancelled"', status_code=200)

    def test_unused_meeting(self):
        self.meeting.state = 'unused'
        self.meeting.save()

        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, 'No fue reservada', status_code=200)
        self.assertContains(response, 'icon-cancelled"', status_code=200)

    def test_details_not_visible(self):
        response = self.client.get('/dude/meetings/1/')
        self.assertNotContains(response, 'Detalles', status_code=200)

    def test_details_not_visible_to_non_participants(self):
        self._login_user()
        self.meeting.state = 'reserved'
        self.meeting.protege = self.user2
        self.meeting.save()
        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, 'Detalles', status_code=200)

    def test_details_visible(self):
        self._login_user()
        self.meeting.state = 'reserved'
        self.meeting.save()
        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, 'Detalles', status_code=200)

    def test_meeting_details_not_visible_if_reserved(self):
        '''
        Participant emails and meeting.format details should
        only be visible after the meeting is confirmed
        '''
        self._login_user()
        self.meeting.state = 'reserved'
        self.meeting.format = 'skype'
        self.meeting.save()
        response = self.client.get('/dude/meetings/1/')
        self.assertNotContains(response, 'dudeskype', status_code=200)
        self.assertNotContains(response, 'thedude@example.com', status_code=200)

    def test_meeting_details_visible_if_confirmed(self):
        self._login_user()
        self.meeting.state = 'confirmed'
        self.meeting.format = 'skype'
        self.meeting.save()
        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, 'dudeskype', status_code=200)
        self.assertContains(response, 'thedude@example.com', status_code=200)

    def test_comments_visible(self):
        ctype = ContentType.objects.get(app_label='meetings', model='meeting')
        Comment.objects.create(
            user=self.dude, comment='This is a test comment',
            content_type=ctype, object_id=self.meeting.id)

        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, 'This is a test comment', status_code=200)

    def test_create_comment(self):
        self._login_user()
        data = {'comment': 'New test comment'}
        response = self.client.post('/dude/meetings/1/comment/', data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dude/meetings/1/')

        response = self.client.get('/dude/meetings/1/')
        self.assertContains(response, 'New test comment', status_code=200)
