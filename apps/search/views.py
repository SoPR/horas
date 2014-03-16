import operator
from functools import reduce

from django.views.generic import ListView
from django.db.models import Q, Count

from taggit.models import Tag

from ..profiles.models import User


class SearchView(ListView):
    queryset = User.objects.all().order_by('-date_joined')
    template_name = 'search/search.html'

    def get_context_data(self):
        context = super(SearchView, self).get_context_data()

        tags = Tag.objects.all().annotate(
            num_times=Count('taggit_taggeditem_items')
        ).filter(num_times__gt=0).order_by('-num_times')

        cities = User.objects.exclude(
            city='').values_list('city', flat=True).distinct()

        context.update({
            'tags': tags[:20],
            'cities': cities[:20],
            'search_term': self.request.GET.get('q', '')
        })

        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        search_term = self.request.GET.get('q')

        if search_term:
            search_args = []
            queries = (
                'first_name__istartswith',
                'last_name__istartswith',
                'tags__name__icontains',
                'city__icontains',
                'state__icontains',
            )

            for term in search_term.split():
                for query in queries:
                    search_args.append(Q(**{query: term}))

            return queryset.filter(
                reduce(operator.or_, search_args)).distinct()

        return queryset[:9]
