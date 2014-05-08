# -*- coding: utf-8 -*-
from apps.meetings.tests import MeetingBaseTestCase


class MeetingDetailViewTestCase(MeetingBaseTestCase):
    def test_meeting_should_be_under_the_username_of_the_mentor(self):
        response = self.client.get('/dude/meetings/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name,
                         ['meetings/meeting_detail.html'])
