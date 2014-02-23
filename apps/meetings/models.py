from django.db import models
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
        unique_together = (
            ('mentor', 'datetime'),
        )

    def __str__(self):
        return '{} - {}'.format(self.mentor, self.datetime)

    def reserve(self, user, message):
        self.protege = user
        self.message = message
        self.save()

    def cancel(self, user):
        self.cancelled_by = user
        self.save()
