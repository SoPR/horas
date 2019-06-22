import pytz
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import gettext_lazy as _


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')

        if tzname:
            timezone.activate(pytz.timezone(tzname))

        elif request.user.is_authenticated:
            try:
                tzname = request.user.timezone
                timezone.activate(pytz.timezone(tzname))
            except Exception as e:
                print('Failed to set timezone', e)
        else:
            timezone.deactivate()


class EnsureCompleteProfileMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user

        if user.is_authenticated:
            skip_urls = [
                str(reverse_lazy('profile_update', args=[user.username])),
                str(reverse_lazy('account_logout')),
                str(reverse_lazy('admin:index'))
            ]

            is_skip_url = any([
                request.path.startswith(url) for url in skip_urls
            ])

            if not user.has_complete_profile() and not is_skip_url:
                message = _('Debes completar tu perfil para continuar')
                messages.info(request, message)
                return HttpResponseRedirect(skip_urls[0])
