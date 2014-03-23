from datetime import timedelta

from django.db import models
from django.utils.timezone import get_current_timezone
from django.utils.formats import date_format

from notification import models as notification

from ..core.models import BaseModel


class Meeting(BaseModel):
    mentor = models.ForeignKey('profiles.User', related_name='mentors')
    protege = models.ForeignKey('profiles.User', blank=True, null=True,
                                related_name='proteges')
    cancelled_by = models.ForeignKey('profiles.User', blank=True, null=True,
                                     related_name='+')

    message = models.TextField(blank=True)

    datetime = models.DateTimeField()

    class Meta:
        ordering = ('-datetime',)

    def __str__(self):
        return '{} - {}'.format(self.mentor, self.datetime)

    def reserve(self, user, message):
        self.protege = user
        self.message = message
        self.save()

        notification.send(
            [self.mentor],
            'reserved_meeting_slot',
            {'meeting': self})

    def cancel(self, user):
        self.cancelled_by = user
        self.save()

        self.mentor.create_meeting_slot()

        notification.send(
            [self.mentor],
            'cancel_meeting',
            {'meeting': self})

    def get_time_range_text(self):
        tz = get_current_timezone()
        start_datetime = self.datetime.astimezone(tz)

        start_time = start_datetime.time()
        end_time = (start_datetime + timedelta(hours=1)).time()

        start_time_fmt = date_format(start_time, 'TIME_FORMAT')
        end_time_fmt = date_format(end_time, 'TIME_FORMAT')

        return '{0} - {1} ({2})'.format(start_time_fmt, end_time_fmt, start_datetime.tzname())
