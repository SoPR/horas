from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_noop as _
from django.db.models import signals

from notification import models as notification

class Command(BaseCommand):

    def handle(self, *args, **options):
        notification.create_notice_type("create_meeting_slot", _("Meeting slot created"), _("your new slot is ready"))
        notification.create_notice_type("reserved_meeting_slot", _("Meeting has been accepted"), _("your meeting has accepted"))
        notification.create_notice_type("cancel_meeting", _("Meeting cancelled"), _("your meeting has been cancelled"))
        notification.create_notice_type("pre_meeting_reminder", _("Your upcoming meeting"), _("your meetings starts in 24 hours"))
        notification.create_notice_type("post_meeting_feedback_request", _("Let us know"), _("how did your meeting go?"))

        self.stdout.write('--> Created notice types')
