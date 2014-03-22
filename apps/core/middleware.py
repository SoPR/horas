import pytz
from django.utils import timezone

class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')

        if tzname:
            timezone.activate(pytz.timezone(tzname))

        elif request.user.is_authenticated():
            try:
                tzname = request.user.timezone
                timezone.activate(pytz.timezone(tzname))
            except Exception as e:
                print('Failed to set timezone', e)
        else:
            timezone.deactivate()
