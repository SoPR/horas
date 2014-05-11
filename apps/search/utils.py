import re


def normalize_query(query_string, findterms=None, normspace=None):
    """
    Splits the query string in invidual keywords, getting rid of
    unecessary spaces and grouping quoted words together.

    Example:
    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
    ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    """

    if not findterms:
        findterms = re.compile(r'"([^"]+)"|(\S+)').findall

    if not normspace:
        normspace = re.compile(r'\s{2,}').sub

    terms = findterms(query_string)

    return [normspace(' ', (t[0] or t[1]).strip()) for t in terms]
