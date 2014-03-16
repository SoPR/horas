import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.loading import get_model
from django.utils.timezone import now, utc
from django.core.urlresolvers import reverse_lazy

from notification import models as notification
from taggit.managers import TaggableManager

from .utils import get_gravatar_url
from .fields import DaysOfWeekField


class User(AbstractUser):
    '''
    Defines our custom user model.
    '''
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
        Meeting = get_model('meetings', 'Meeting')

        today = now().date()
        delta = datetime.timedelta((self.day_of_week - today.weekday()) % 7)

        next_slot_date = today + delta
        next_slot = datetime.datetime.combine(
            next_slot_date, self.start_time).replace(tzinfo=utc)

        meeting_slot = Meeting.objects.create(mentor=self, datetime=next_slot)

        # Notify user
        notification.send(
            [self],
            'create_meeting_slot',
            {'meeting': meeting_slot})
