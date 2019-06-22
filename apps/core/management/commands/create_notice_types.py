from django.core.management.base import BaseCommand
from django.utils.translation import gettext_noop as _
from pinax.notifications.models import NoticeType


class Command(BaseCommand):
    def handle(self, *args, **options):
        NoticeType.create(
            "create_meeting_slot",
            _("Periodo de reunion creada"),
            _("tu periodo de reunion esta lista"),
        )

        NoticeType.create(
            "reserved_meeting_slot",
            _("Reunion aceptada"),
            _("tu reunion ha sido aceptada"),
        )

        NoticeType.create(
            "cancelled_by_mentor",
            _("Reunion cancelada por el mentor"),
            _("tu reunion ha sido cancelada"),
        )

        NoticeType.create(
            "cancelled_by_protege",
            _("Reunion cacelada por aprendiz"),
            _("your meeting has been cancelled"),
        )

        NoticeType.create(
            "confirmed_meeting",
            _("Reunion confirmada"),
            _("su reunion ha sido confirmada"),
        )

        NoticeType.create(
            "post_meeting_mentor", _("Dejenos saber"), _("como le fue en su reunion?")
        )

        NoticeType.create(
            "post_meeting_protege", _("Dejenos saber"), _("como le fue en su reunion?")
        )

        NoticeType.create(
            "comment", _("Comentario nuevo"), _("tienes un nuevo comentario")
        )

        self.stdout.write("--> Created notice types")
