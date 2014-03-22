from datetime import datetime
import pytz

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.loading import get_model
from django.utils.timezone import now, get_default_timezone, make_aware
from django.core.urlresolvers import reverse_lazy

from django.conf import settings

from notification import models as notification
from taggit.managers import TaggableManager

from .utils import get_gravatar_url
from .fields import DaysOfWeekField
from ..meetings.utils import next_weekday


class User(AbstractUser):
    '''
    Defines our custom user model.
    '''

    PRETTY_TIMEZONE_CHOICES = [('', '--- Select ---')]

    for tz in pytz.common_timezones:
        now = datetime.now(pytz.timezone(tz))
        PRETTY_TIMEZONE_CHOICES.append(
            (tz, ' %s (GMT%s)' % (tz, now.strftime('%z'))))

    # Public profile information
    featured = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    twitter_username = models.CharField(blank=True, max_length=50)
    facebook_username = models.CharField(blank=True, max_length=50)
    github_username = models.CharField(blank=True, max_length=50)
    website_url = models.URLField(blank=True, max_length=50)
    gravatar_url = models.URLField(blank=True)
    is_gravatar_verified = models.BooleanField(default=False)
    city = models.CharField(blank=True, max_length=50)
    state = models.CharField(blank=True, max_length=50)

    # Meeting availability
    day_of_week = DaysOfWeekField(blank=True, null=True, db_index=True)
    start_time = models.TimeField(null=True, blank=True)
    timezone = models.CharField(max_length=255,
                                default=settings.HORAS_DEFAULT_TZ,
                                choices=PRETTY_TIMEZONE_CHOICES)

    # Kept private until meeting
    phone = models.CharField(blank=True, max_length=50)
    skype = models.CharField(blank=True, max_length=50)
    google = models.CharField(blank=True, max_length=50)
    jitsi = models.CharField(blank=True, max_length=50)
    address = models.TextField(blank=True)

    tags = TaggableManager(blank=True)

    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.gravatar_url:
            self.gravatar_url = get_gravatar_url(self.email)

        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('profile_detail', args=[self.username])

    def get_tiny_name(self):
        return '{0}. {1}'.format(self.first_name[0], self.last_name)

    def get_location(self):
        if self.city and self.state:
            return '{0}, {1}'.format(self.city, self.state)
        elif self.city:
            return self.city
        elif self.state:
            return self.state

    def create_meeting_slot(self):
        if self.timezone and self.day_of_week and self.start_time:
            Meeting = get_model('meetings', 'Meeting')

            user_tz = pytz.timezone(self.timezone)
            date = next_weekday(now(), self.day_of_week)
            next_slot_local = make_aware(
                datetime.combine(date, self.start_time), user_tz)

            next_slot = next_slot_local.astimezone(get_default_timezone())
            meeting_slot, created = Meeting.objects.get_or_create(mentor=self, datetime=next_slot)

            # Notify user
            if created:
                notification.send(
                    [self],
                    'create_meeting_slot',
                    {'meeting': meeting_slot})

            return meeting_slot, created

        return None, False
