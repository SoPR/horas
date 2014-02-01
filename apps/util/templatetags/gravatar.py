from django import template
register = template.Library()

from ..gravatar import get_gravatar as _get_gravatar


@register.simple_tag
def get_gravatar(*args):
    tag = '<img src="{0}" class="gravatar">'.format(_get_gravatar(*args))
    return tag
