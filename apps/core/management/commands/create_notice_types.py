from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_noop as _

from notification import models as notification

class Command(BaseCommand):

    def handle(self, *args, **options):
        notification.create_notice_type('create_meeting_slot',
                                        _('Meeting slot created'),
                                        _('your new slot is ready'))

        notification.create_notice_type('reserved_meeting_slot',
                                        _('Meeting has been accepted'),
                                        _('your meeting has accepted'))

        notification.create_notice_type('cancelled_by_mentor',
                                        _('Meeting cancelled by mentor'),
                                        _('your meeting has been cancelled'))

        notification.create_notice_type('cancelled_by_protege',
                                        _('Meeting cancelled by protege'),
                                        _('your meeting has been cancelled'))

        notification.create_notice_type('confirmed_meeting',
                                        _('Meeting confirmed'),
                                        _('your meeting reservation was confirmed'))

        notification.create_notice_type('post_meeting_mentor',
                                        _('Let us know'),
                                        _('how did your meeting go?'))

        notification.create_notice_type('post_meeting_protege',
                                        _('Let us know'),
                                        _('how did your meeting go?'))

        self.stdout.write('--> Created notice types')
