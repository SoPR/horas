# -*- coding: utf-8 -*-
import os
from datetime import timedelta

from django.db import models
from django.utils.timezone import get_current_timezone, now
from django.utils.formats import date_format
from django.core.urlresolvers import reverse_lazy
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import tweepy
import bitly_api
from django_states.fields import StateField

from ..core.models import BaseModel
from .states import MeetingStateMachine


class Meeting(BaseModel):
    mentor = models.ForeignKey('profiles.User', related_name='mentors')
    protege = models.ForeignKey('profiles.User', blank=True, null=True,
                                related_name='proteges')
    cancelled_by = models.ForeignKey('profiles.User', blank=True, null=True,
                                     related_name='+')

    format = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True)
    datetime = models.DateTimeField()

    # posible state values are documented on states.py
    state = StateField(
        machine=MeetingStateMachine, default='available', db_index=True)

    class Meta:
        ordering = ('-datetime',)

    def __str__(self):
        return '[{}] {} - {}'.format(self.pk, self.mentor, self.datetime)

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

    def get_short_url(self):
        bitly = bitly_api.Connection(
            access_token=os.environ.get('BITLY_ACCESS_TOKEN'))
        return bitly.shorten(self.get_url_with_domain())['url']

    def get_twitter_message(self):
        message = _(u'{0} tiene un espacio de reunión disponible. {1}'.format(
                    self.mentor.get_full_name(), self.get_short_url()))
        return message.encode('utf-8')

    def publish_on_twitter(self):
        auth = tweepy.OAuthHandler(os.environ.get('TWITTER_API_KEY'),
                                   os.environ.get('TWITTER_API_SECRET'))

        auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'),
                              os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))

        api = tweepy.API(auth)
        api.update_status(self.get_twitter_message())


