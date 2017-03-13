from datetime import timedelta

from django.db import models
from django.utils.timezone import now


class StatManager(models.Manager):
    def get_range(self, name, hours=24):
        last_n_hours = [now() - timedelta(hours=hours), now()]
        queryset = super(StatManager, self).get_query_set()
        stats = queryset.filter(name=name, date_created__range=last_n_hours)
        if stats:
            return stats
        return None

    def get_latest(self, name):
        queryset = super(StatManager, self).get_queryset()
        stats = queryset.filter(name=name)
        if stats:
            return stats[0]
        return None

class Stat(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, db_index=True)
    count = models.IntegerField()

    objects = StatManager()

    class Meta:
        ordering = ('-date_created',)

    def __unicode__(self):
        return '{0}: {1}'.format(self.name, self.count)
