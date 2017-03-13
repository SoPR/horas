from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models.signals import post_save
from notification import models as notification

from ..core.models import BaseModel


class Comment(BaseModel):
    user = models.ForeignKey('profiles.User', related_name='users')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    comment = models.TextField()

    def __unicode__(self):
        return '{0}: {1}...'.format(self.user.first_name, self.comment[:50])

    class Meta:
        ordering = ('date_created',)



def comment_saved(sender, instance, created, **kwargs):
    mentor = instance.content_object.mentor
    protege = instance.content_object.protege
    meeting_url = instance.content_object.get_url_with_domain()

    if instance.user == mentor:
        recipient = protege

    elif instance.user == protege:
        recipient = mentor

    if created and recipient:
        notification.send(
            [recipient],
            'comment',
            {'comment': instance,
             'recipient': recipient,
             'meeting_url': meeting_url})

post_save.connect(comment_saved, sender=Comment)
