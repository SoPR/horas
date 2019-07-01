from datetime import timedelta

from django.utils.timezone import now

from apps.meetings.models import Meeting
from apps.meetings.tests import MeetingBaseTestCase


class UpdateMeetingsCommandTestCase(MeetingBaseTestCase):
    def test_should_flag_available_in_past_as_unused(self):
        m = Meeting.objects.create(
            state="available",
            mentor=self.dude,
            datetime=now() - timedelta(hours=1, seconds=1),
        )

        self.assertEqual(Meeting.objects.filter(state="unused").count(), 0)
        self.assertEqual(Meeting.objects.filter(state="available").count(), 2)

        self.call_command("update_meetings")

        self.assertEqual(Meeting.objects.get(pk=m.id).state, "unused")
        self.assertEqual(Meeting.objects.filter(state="unused").count(), 1)
        self.assertEqual(Meeting.objects.filter(state="available").count(), 1)

    def test_should_create_missing_meetings(self):
        Meeting.objects.all().delete()
        self.assertEqual(Meeting.objects.filter(state="available").count(), 0)
        self.call_command("update_meetings")
        self.assertEqual(Meeting.objects.filter(state="available").count(), 1)
