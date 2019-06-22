from datetime import timedelta
from enum import Enum

from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse_lazy
from django.utils.formats import date_format
from django.utils.timezone import get_current_timezone, now
from django.utils.translation import gettext_lazy as _
from django_fsm import FSMField, TransitionNotAllowed, transition
from pinax.notifications import models as notifications

from ..core.models import BaseModel


class Meeting(BaseModel):
    class STATES(Enum):
        """
        Possible states
        ---------------

        available:
            A new meeting.

        reserved:
            A meeting that was available and reserved by mentee.

        confirmed:
            A meeting that was reserved by a mentee and later accepted
            by the meeting's mentor.

        cancelled:
            A meeting that was either reserved or confirmed and
            then cancelled by the mentor or mentee.

        unused:
            at least 1 hour have passed from the meeting's start datetime
            and the meeting is still in the available state, meaning
            it was not reserved by a mentee.

        deleted:
            A meeting in available state can be transitioned to deleted
            by the system after a user updates his/her meeting settings.
            This transition will produce a new available meeting.
        """

        ANY = "*"
        UNUSED = "unused"
        DELETED = "deleted"
        RESERVED = "reserved"
        AVAILABLE = "available"
        CONFIRMED = "confirmed"
        CANCELLED = "cancelled"

    mentor = models.ForeignKey(
        "profiles.User", related_name="mentors", on_delete=models.CASCADE
    )
    protege = models.ForeignKey(
        "profiles.User",
        blank=True,
        null=True,
        related_name="proteges",
        on_delete=models.CASCADE,
    )
    cancelled_by = models.ForeignKey(
        "profiles.User",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.CASCADE,
    )

    format = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True)
    datetime = models.DateTimeField()

    state = FSMField(default="available")

    class Meta:
        ordering = ("-datetime",)

    def __str__(self):
        return f"{self.pk}-{self.mentor}-{self.datetime}-{self.state}"

    def get_absolute_url(self):
        return reverse_lazy("meeting_detail", args=[self.mentor.username, self.pk])

    def get_url_with_domain(self):
        domain = Site.objects.get_current().domain
        return f"{settings.PROTOCOL}://{domain}{self.get_absolute_url()}"

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

        start_time_fmt = date_format(start_time, "TIME_FORMAT")
        end_time_fmt = date_format(end_time, "TIME_FORMAT")

        return f"{start_time_fmt} - {end_time_fmt} ({start_datetime.tzname()})"

    # state machine transitions
    @transition(
        field=state,
        source=STATES.AVAILABLE.value,
        target=STATES.RESERVED.value,
        permission=lambda instance, user: instance.mentor != user,
    )
    def reserve(self, reserved_by):
        if reserved_by == self.mentor:
            raise TransitionNotAllowed

        self.protege = reserved_by

        notifications.send([self.mentor], "reserved_meeting_slot", {"meeting": self})

    @transition(
        field=state,
        source=STATES.RESERVED.value,
        target=STATES.CONFIRMED.value,
        permission=lambda instance, user: instance.mentor == user,
    )
    def confirm(self, confirmed_by):
        if confirmed_by != self.mentor:
            raise TransitionNotAllowed

        notifications.send([self.protege], "confirmed_meeting", {"meeting": self})

    @transition(
        field=state,
        source=[STATES.RESERVED.value, STATES.CONFIRMED.value],
        target=STATES.CANCELLED.value,
        permission=lambda instance, user: user in [instance.mentor, instance.protege],
    )
    def cancel(self, cancelled_by):
        if cancelled_by not in [self.mentor, self.protege]:
            raise TransitionNotAllowed

        self.cancelled_by = cancelled_by

        if self.cancelled_by_mentor():
            # Send message to mentee
            notifications.send([self.protege], "cancelled_by_mentor", {"meeting": self})

        if self.cancelled_by_protege():
            # Send message to mentor
            notifications.send([self.mentor], "cancelled_by_protege", {"meeting": self})

        self.mentor.get_or_create_meeting()

    @transition(field=state, source=STATES.AVAILABLE.value, target=STATES.UNUSED.value)
    def flag_unused(self):
        pass

    @transition(field=state, source=STATES.AVAILABLE.value, target=STATES.DELETED.value)
    def flag_deleted(self):
        pass
