from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_ical.views import ICalFeed

from apps.meetings.models import Meeting


class ProfileCalendarFeed(ICalFeed):
    product_id = "-//1hora.org//1hora//EN"
    timezone = "UTC"
    title = _("1hora.org")
    description = _("Calendario de reuniones de 1hora.org.")

    def get_object(self, request, username):
        return (
            Meeting.objects.select_related("mentor", "protege")
            .filter(Q(protege__username=username) | Q(mentor__username=username))
            .filter(
                Q(state=Meeting.STATES.RESERVED) | Q(state=Meeting.STATES.CONFIRMED)
            )
        )

    def items(self, objects):
        return objects

    def item_title(self, item):
        if item.state == Meeting.STATES.CONFIRMED:
            state = _("Confirmada")
        elif item.state == Meeting.STATES.RESERVED:
            state = _("Reservada")

        return f"[1hora.org: {state}]: {item.mentor.get_full_name()} con {item.protege.get_full_name()}"

    def item_description(self, item):
        return item.message

    def timezone(self):
        return

    def item_start_datetime(self, item):
        return item.datetime

    def item_end_datetime(self, item):
        return item.get_end_datetime()

    def item_guid(self, item):
        return f"{item.id}@meetings.1hora.org"
