from django.db import models
from django.utils.translation import ugettext_lazy as _

DAYS_OF_WEEK = (
    (0, _('Monday')),
    (1, _('Tuesday')),
    (2, _('Wednesday')),
    (3, _('Thursday')),
    (4, _('Friday')),
    (5, _('Saturday')),
    (6, _('Sunday')),
)


class DaysOfWeekField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = DAYS_OF_WEEK
        kwargs['max_length'] = 1
        super().__init__(*args, **kwargs)

    def south_field_triple(self):
        """
        Returns a suitable description of this field for South.
        """
        from south.modelsinspector import introspector

        field_class = "django.db.models.fields.IntegerField"
        args, kwargs = introspector(self)

        return (field_class, args, kwargs)
