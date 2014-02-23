from django.db import models

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
