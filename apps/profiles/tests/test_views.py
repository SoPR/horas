from datetime import timedelta

from django.utils.timezone import now

from apps.core.tests import BaseTestCase
from apps.meetings.models import Meeting


class UserProfileCompletionTestCase(BaseTestCase):
    def test_login_should_redirect_to_profile(self):
        response = self._login_user()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/dude/")

    def test_incomplete_profile_should_redirect_to_profile(self):
        # make user incomplete
        self.dude.first_name = ""
        self.dude.save()

        self._login_user()

        response = self.client.get("/es/stats/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/es/dude/update/")

    def test_complete_profile_shouldnt_redirect_to_profile(self):
        self._login_user()
        response = self.client.get("/es/stats/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["stats/stats.html"])

    def test_complete_profile_should_redirect_from_home_to_search(self):
        self._login_user()
        response = self.client.get("/es/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/es/search/")


class UserUpdateViewTestCase(BaseTestCase):
    def test_submit_incomplete_form_should_display_error(self):
        self._login_user()
        response = self.client.post("/es/dude/update/", {})
        self.assertContains(
            response, '<ul class="errorlist nonfield">', status_code=200
        )

    def test_submit_complete_form_should_redirect_to_profile_with_msg(self):
        self._login_user()
        data = {
            "first_name": "Juan",
            "last_name": u"Áéíóú",
            "bio": "Bio",
            "tags": "one, two, three",
            "city": "San Juan",
            "state": "PR",
            "skype": "skypename",
            "day_of_week": "0",
            "start_time": "00:00:00",
            "timezone": "America/Puerto_Rico",
        }
        response = self.client.post("/es/dude/update/", data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/es/dude/")

        response = self.client.get("/es/dude/")
        self.assertContains(
            response, "alert alert-success alert-dismissable", status_code=200
        )


class UserDetailViewTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        # Available
        Meeting.objects.create(
            mentor=self.dude, protege=self.dude, datetime=now() + timedelta(days=1)
        )
        # Next
        Meeting.objects.create(
            mentor=self.dude,
            protege=self.dude,
            datetime=now() + timedelta(days=1),
            state="confirmed",
        )
        # Past
        Meeting.objects.create(
            mentor=self.dude,
            protege=self.dude,
            datetime=now() - timedelta(days=1),
            state="unused",
        )

    def test_correct_meetings_in_context_data(self):
        response = self.client.get("/es/dude/")
        meetings = response.context_data["object"]["meetings"]

        self.assertEqual(len(meetings["available"]), 1)
        self.assertEqual(len(meetings["next"]), 1)
        self.assertEqual(len(meetings["past"]), 1)

        self.assertEqual(meetings["available"][0].state, "available")
        self.assertEqual(meetings["next"][0].state, "confirmed")
        self.assertEqual(meetings["past"][0].state, "unused")

    def test_profile_user_in_context_data(self):
        response = self.client.get("/es/dude/")
        profile_user = response.context_data["object"]["profile_user"]
        self.assertEqual(profile_user, self.dude)
