# -*- coding: utf-8 -*-
from datetime import timedelta

from django.conf import settings
from django.contrib.sites.models import Site
from django.urls import reverse_lazy
from django.db import models
from django.utils.formats import date_format
from django.utils.timezone import get_current_timezone, now
from django_states.fields import StateField

from ..core.models import BaseModel
from .states import MeetingStateMachine


class Meeting(BaseModel):
    mentor = models.ForeignKey('profiles.User', related_name='mentors', on_delete=models.CASCADE)
    protege = models.ForeignKey('profiles.User', blank=True, null=True,
                                related_name='proteges', on_delete=models.CASCADE)
    cancelled_by = models.ForeignKey('profiles.User', blank=True, null=True,
                                     related_name='+', on_delete=models.CASCADE)

    format = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True)
    datetime = models.DateTimeField()

    # posible state values are documented on states.py
    state = StateField(
        machine=MeetingStateMachine, default='available', db_index=True)

    class Meta:
        ordering = ('-datetime',)

    def __str__(self):
        return '{0}-{1}-{2}-{3}'.format(self.pk, self.mentor,
                                        self.datetime, self.state)

    def get_absolute_url(self):
        return reverse_lazy('meeting_detail',
                            args=[self.mentor.username, self.pk])

    def get_url_with_domain(self):
        domain = Site.objects.get_current().domain
        return '{0}://{1}{2}'.format(settings.PROTOCOL,
                                     domain, self.get_absolute_url())

    def cancelled_by_mentor(self):
        return self.cancelled_by == self.mentor

    def cancelled_by_protege(self):
        return self.cancelled_by == self.protege

    def get_end_datetime(self):
        return self.datetime + timedelta(hours=1)

    def is_in_past(self):
        # I actually like this method name
        return now() > self.get_end_datetime()

    def get_time_range_string(self):
        tz = get_current_timezone()
        start_datetime = self.datetime.astimezone(tz)

        start_time = start_datetime.time()
        end_time = (start_datetime + timedelta(hours=1)).time()

        start_time_fmt = date_format(start_time, 'TIME_FORMAT')
        end_time_fmt = date_format(end_time, 'TIME_FORMAT')

        return '{0} - {1} ({2})'.format(start_time_fmt,
                                        end_time_fmt, start_datetime.tzname())
