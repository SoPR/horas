import hmac
from base64 import b64decode, b64encode
from hashlib import sha256

from django.conf import settings
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.utils.http import urlencode


def single_sign_on(request):
    sso = request.GET.get("sso", None)
    sig = request.GET.get("sig", None)

    if sso and sig:
        # we have both needed params
        nonce = b64decode(sso).split("=")[1]
        payload_sig = hmac.new(settings.SSO_SECRET_KEY, sso, sha256).hexdigest()

        if payload_sig == sig:
            # sig is valid

            if request.user.is_authenticated:
                # user is authenticated
                user = request.user

                payload = {
                    "nonce": nonce,
                    "email": user.email,
                    "external_id": user.id,
                    "username": user.username,
                    "name": user.get_full_name(),
                    "return_url": reverse("profile_detail", args=[user.username]),
                }

                new_payload = b64encode(urlencode(payload))
                new_sig = hmac.new(
                    settings.SSO_SECRET_KEY, new_payload, sha256
                ).hexdigest()

                params = {"sso": new_payload, "sig": new_sig}
                redirect_url = settings.DISCOURSE_SSO_REDIRECT_URL + urlencode(params)

                return HttpResponseRedirect(redirect_url)

            else:
                # we don't have a valid user redirect to login
                # TODO: use next to handle redirections
                return HttpResponseRedirect(reverse("account_login"))

    # 404 if we fail
    return HttpResponseNotFound()
