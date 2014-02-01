import hashlib
from django.conf import settings


def get_gravatar(email, size=80):
    url_prefix = getattr(settings, 'GRAVATAR_URL_PREFIX', 'https://secure.gravatar.com/')
    default_image = getattr(settings, 'GRAVATAR_DEFAULT_IMAGE', 'retro')
    rating = getattr(settings, 'GRAVATAR_DEFAULT_RATING', 'g')

    email = email.encode('utf8')
    hash = hashlib.md5(email.lower()).hexdigest()
    url = '{0}avatar/{1}?s={2}&d={3}&r={4}'
    return url.format(url_prefix, hash, size, default_image, rating)
