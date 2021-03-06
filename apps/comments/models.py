from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from pinax.notifications import models as notifications

from ..core.models import BaseModel


class Comment(BaseModel):
    user = models.ForeignKey(
        "profiles.User", related_name="users", on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.first_name,}: {self.comment[:50]}..."

    class Meta:
        ordering = ("date_created",)


def comment_saved(sender, instance, created, **kwargs):
    mentor = instance.content_object.mentor
    protege = instance.content_object.protege
    meeting_url = instance.content_object.get_url_with_domain()

    if instance.user == mentor:
        recipient = protege

    elif instance.user == protege:
        recipient = mentor

    if created and recipient:
        notifications.send(
            [recipient],
            "comment",
            {"comment": instance, "recipient": recipient, "meeting_url": meeting_url},
        )


post_save.connect(comment_saved, sender=Comment)
