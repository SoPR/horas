from django.db import models
from django.utils.translation import gettext_lazy as _

DAYS_OF_WEEK = (
    (0, _("Lunes")),
    (1, _("Martes")),
    (2, _("Miércoles")),
    (3, _("Jueves")),
    (4, _("Viernes")),
    (5, _("Sábado")),
    (6, _("Domingo")),
)


class DaysOfWeekField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs["choices"] = DAYS_OF_WEEK
        # kwargs['max_length'] = 1
        super().__init__(*args, **kwargs)
