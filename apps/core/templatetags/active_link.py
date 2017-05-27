import re

from django import template

register = template.Library()


@register.simple_tag
def active_link(request, pattern):
    '''
    Simple template tag that will return the string active if the passed
    pattern is found in the current url. We user this to highlight the
    current menu item.
    '''
    path = '/{}/'.format(request.path.split('/')[1])

    if re.search(pattern, path):
        return 'active'
    return ''
