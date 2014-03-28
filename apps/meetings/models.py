from datetime import timedelta

from django.db import models
from django.utils.timezone import get_current_timezone, now
from django.utils.formats import date_format

from django_states.fields import StateField

from ..core.models import BaseModel
from .states import MeetingStateMachine


class Meeting(BaseModel):
    mentor = models.ForeignKey('profiles.User', related_name='mentors')
    protege = models.ForeignKey('profiles.User', blank=True, null=True,
                                related_name='proteges')
    cancelled_by = models.ForeignKey('profiles.User', blank=True, null=True,
                                     related_name='+')

    message = models.TextField(blank=True)

    datetime = models.DateTimeField()

    # posible state values are documented on states.py
    state = StateField(
        machine=MeetingStateMachine, default='available', db_index=True)

    class Meta:
        ordering = ('-datetime',)

    def __str__(self):
        return '{} - {}'.format(self.mentor, self.datetime)

    def is_in_past(self):
        # I actually like this method name
        return now() > (self.datetime + timedelta(hours=1))

    def get_time_range_text(self):
        tz = get_current_timezone()
        start_datetime = self.datetime.astimezone(tz)

        start_time = start_datetime.time()
        end_time = (start_datetime + timedelta(hours=1)).time()

        start_time_fmt = date_format(start_time, 'TIME_FORMAT')
        end_time_fmt = date_format(end_time, 'TIME_FORMAT')

        return '{0} - {1} ({2})'.format(start_time_fmt, end_time_fmt, start_datetime.tzname())
