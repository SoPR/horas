from django.db import models
from django.utils.translation import ugettext_lazy as _

DAYS_OF_WEEK = (
    (0, _('Sunday')),
    (1, _('Monday')),
    (2, _('Tuesday')),
    (3, _('Wednesday')),
    (4, _('Thursday')),
    (5, _('Friday')),
    (6, _('Saturday'))
)


class DaysOfWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = DAYS_OF_WEEK
        kwargs['max_length'] = 1
        super().__init__(*args, **kwargs)
