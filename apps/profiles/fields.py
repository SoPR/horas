# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

DAYS_OF_WEEK = (
    (0, _('Lunes')),
    (1, _('Martes')),
    (2, _(u'Miércoles')),
    (3, _('Jueves')),
    (4, _('Viernes')),
    (5, _(u'Sábado')),
    (6, _('Domingo')),
)


class DaysOfWeekField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = DAYS_OF_WEEK
        kwargs['max_length'] = 1
        super(DaysOfWeekField, self).__init__(*args, **kwargs)

    def south_field_triple(self):
        """
        Returns a suitable description of this field for South.
        """
        from south.modelsinspector import introspector

        field_class = "django.db.models.fields.IntegerField"
        args, kwargs = introspector(self)

        return (field_class, args, kwargs)
