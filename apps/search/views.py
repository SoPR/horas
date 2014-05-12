import urllib

from django.views.generic import ListView
from django.db.models import Count
from django.utils.http import urlquote_plus

from taggit.models import Tag

from ..profiles.models import User


class SearchView(ListView):
    queryset = User.objects.all().order_by('-date_joined')
    template_name = 'search/search.html'
    paginate_by = 12

    def get_context_data(self):
        context = super(SearchView, self).get_context_data()

        tags = Tag.objects.all().annotate(
            num_times=Count('taggit_taggeditem_items')
        ).filter(num_times__gt=0).order_by('-num_times')

        cities = User.objects.exclude(
            city='').values_list('city', flat=True).distinct()

        urlencoded_cities = []

        for city in cities[:20]:
            urlencoded_cities.append({
                'value': city,
                'term': urlquote_plus(city)
            })

        context.update({
            'tags': tags[:20],
            'cities': urlencoded_cities,
            'search_term': urllib.unquote_plus(self.request.GET.get('q', ''))
        })

        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        search_term = self.request.GET.get('q')

        if search_term:
            return User.objects.search(search_term).order_by('-date_joined')

        return [q for q in queryset if q.has_complete_profile()]
