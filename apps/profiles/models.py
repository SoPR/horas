from django.db import models
from django.contrib.auth.models import AbstractUser

from .fields import DaysOfWeekField


class User(AbstractUser):
    '''
    Defines our custom user model.
    '''
    # Public profile information
    bio = models.TextField(blank=True)
    twitter_username = models.CharField(blank=True, max_length=50)
    facebook_username = models.CharField(blank=True, max_length=50)
    github_username = models.CharField(blank=True, max_length=50)
    website_url = models.URLField(blank=True, max_length=50)

    # Meeting availability
    day_of_week = DaysOfWeekField(blank=True, db_index=True)
    start_time = models.TimeField(null=True, blank=True)

    # Kept private until meeting
    phone = models.CharField(blank=True, max_length=50)
    skype = models.CharField(blank=True, max_length=50)
    google = models.CharField(blank=True, max_length=50)
    jitsi = models.CharField(blank=True, max_length=50)
    address = models.TextField(blank=True)

    date_updated = models.DateTimeField(auto_now=True)

    def get_tiny_name(self):
        return '{0}. {1}'.format(self.first_name[0], self.last_name)
