from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_noop as _

from pinax.notifications.models import NoticeType


class Command(BaseCommand):

    def handle(self, *args, **options):
        NoticeType.create(
            'create_meeting_slot',
            _('Meeting slot created'),
            _('your new slot is ready')
        )

        NoticeType.create(
            'reserved_meeting_slot',
            _('Meeting has been accepted'),
            _('your meeting has accepted')
        )

        NoticeType.create(
            'cancelled_by_mentor',
            _('Meeting cancelled by mentor'),
            _('your meeting has been cancelled')
        )

        NoticeType.create(
            'cancelled_by_protege',
            _('Meeting cancelled by protege'),
            _('your meeting has been cancelled')
        )

        NoticeType.create(
            'confirmed_meeting',
            _('Meeting confirmed'),
            _('your meeting reservation was confirmed')
        )

        NoticeType.create(
            'post_meeting_mentor',
            _('Let us know'),
            _('how did your meeting go?')
        )

        NoticeType.create(
            'post_meeting_protege',
            _('Let us know'),
            _('how did your meeting go?')
        )

        NoticeType.create(
            'comment',
            _('New comment'),
            _('you have a new comment')
        )

        self.stdout.write('--> Created notice types')
