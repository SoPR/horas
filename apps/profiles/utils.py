import hashlib


def get_gravatar_url(email):
    email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return "http://www.gravatar.com/avatar/{}".format(email_hash)
