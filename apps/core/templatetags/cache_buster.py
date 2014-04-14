import os
import time

from django import template
from django.conf import settings

register = template.Library()


@register.tag(name="cache_buster")
def do_cache_buster(parser, token):
    return CacheBusterTag()


class CacheBusterTag(template.Node):

    head = None

    @staticmethod
    def _get_buster():
        if settings.ENVIRONMENT == 'development':
            return int(time.time())
        else:
            ref = os.getenv('HEAD_COMMIT_ID')

            if ref:
                # Use the first 7 chars of SHA like git log pretty format
                short_ref = ref[:7]
                return unicode(short_ref)
            else:
                # Missing HEAD_COMMIT_ID environment variable
                return 'BAD_HEAD_COMMIT_ID'

    @staticmethod
    def get_head_cached():
        if settings.ENVIRONMENT == 'development' or not CacheBusterTag.head:
            CacheBusterTag.head = CacheBusterTag._get_buster()
        return CacheBusterTag.head

    def render(self, context):
        return CacheBusterTag.get_head_cached()
