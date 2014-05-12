import urllib

from django.db import models, connection
from django.contrib.auth.models import UserManager
from django.db.models import Q

from djorm_pgfulltext import models as search_models

from ..search.utils import normalize_query


class UserSearchManager(search_models.SearchManagerMixIn, UserManager):
    def __init__(self, *args, **kwargs):
        super(UserSearchManager, self).__init__(
            fields=('first_name', 'last_name'),
            config='pg_catalog.spanish',
            search_field='search_index',
            auto_update_search_field=(connection.vendor == 'postgresql')
        )

    def contribute_to_class(self, cls, name):
        """
        Custom version of SearchManagerMixin.contribute_to_class to avoid
        setting up manager if connection vendor is not `postgresql`.
        """
        if connection.vendor != 'postgresql':
            super(search_models.SearchManagerMixIn,
                  self).contribute_to_class(cls, name)

        # Attach this manager as _fts_manager in the model class.
        if not getattr(cls, '_fts_manager', None):
            cls._fts_manager = self

        # Add 'update_search_field' instance method,
        # that calls manager's update_search_field.
        if not getattr(cls, 'update_search_field', None):
            def update_search_field(self, using=None, config=None):
                self._fts_manager.update_search_field(
                    pk=self.pk, using=using, config=config)
            setattr(cls, 'update_search_field', update_search_field)

        if self.auto_update_search_field:
            models.signals.post_save.connect(
                search_models.auto_update_search_field_handler, sender=cls)

        super(search_models.SearchManagerMixIn,
              self).contribute_to_class(cls, name)

    def search(self, search_term, **kwargs):
        """
        Custom version of SearchManagerMixin.search that implements
        searching for tags, city, and name. If connection vendor is
        `postgresql` unaccented full-text search is used for the
        user's first and last name.
        """
        tokens = normalize_query(search_term)
        queryset = self
        query = None
        token_dict = {}
        name_token = []

        for token in tokens:
            _token = urllib.unquote_plus(token).split(':', 1)

            if len(_token) == 1:
                name_token.append(_token[0])
            else:
                token_dict[_token[0]] = _token[1].split(',')

        tag_term = token_dict.get('tag')
        city_term = token_dict.get('city')

        if name_token:
            if connection.vendor == 'postgresql':
                name_term = ' '.join(name_token)
                queryset = super(UserSearchManager, self).search(
                    name_term, **kwargs)
            else:
                for term in name_token:
                    name_query = (
                        Q(first_name__istartswith=term) |
                        Q(last_name__istartswith=term)
                    )

                    if query:
                        query = query & name_query
                    else:
                        query = name_query

        if tag_term:
            tag_q = Q(tags__name__in=tag_term)

            if query:
                query = query & tag_q
            else:
                query = tag_q

        if city_term:
            city_q = Q(city__in=city_term)

            if query:
                query = query & city_q
            else:
                query = city_q

        if query:
            return queryset.filter(query).distinct()

        return queryset.distinct()
