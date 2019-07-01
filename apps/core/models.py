from django.db import models
from django.utils.timezone import now


class DateTimeCreatedField(models.DateTimeField):
    """
    DateTimeField that by default, sets editable=False,
    blank=True, default=now.
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("editable", False)
        kwargs.setdefault("blank", True)
        kwargs.setdefault("default", now)
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return "DateTimeField"


class DateTimeModifiedField(DateTimeCreatedField):
    """
    DateTimeField that by default, sets editable=False,
    blank=True, default=datetime.now.

    Sets value to now() on each save of the model.
    """

    def pre_save(self, model, add):
        value = now()
        setattr(model, self.attname, value)
        return value


class BaseModel(models.Model):
    """
    An abstract base class model that provides:
        - date_created
        - date_modified
    """

    date_created = DateTimeCreatedField()
    date_modified = DateTimeModifiedField()

    class Meta:
        get_latest_by = "date_modified"
        ordering = ("-date_modified", "-date_created")
        abstract = True
