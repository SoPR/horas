from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from ..core.models import BaseModel


class Comment(BaseModel):
    user = models.ForeignKey('profiles.User', related_name='users')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    comment = models.TextField()

    def __unicode__(self):
        return '{0}: {1}...'.format(self.user.first_name, self.comment[:50])

    class Meta:
        ordering = ('date_created',)
