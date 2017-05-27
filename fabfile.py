# -*- coding: utf-8 -*-
import os

from fabric.api import env, local

# Get current Git branch
current_git_branch = local('git rev-parse --abbrev-ref HEAD', capture=True)


def development():
    env.env = 'development'
    os.environ['ENVIRONMENT'] = env.env
    os.environ['DJANGO_CONFIGURATION'] = 'Develoment'
    env.domain = 'localhost:8000'


def production():
    env.env = 'production'
    os.environ['ENVIRONMENT'] = env.env
    os.environ['DJANGO_CONFIGURATION'] = 'Production'
    env.remote = 'heroku {}:master'.format(current_git_branch)
    env.heroku_app = 'unahora'
    env.domain = '{}.herokuapp.com'.format(env.heroku_app)


# === Deployment ===
def deploy():
    local('git push {remote} --force'.format(**env))


# === Static ===
def collectstatic():
    # move contents of static/ to a dir named HEAD_COMMIT_ID
    build()
    local('./manage.py collectstatic --noinput')
    if env.env != 'development':
        commit_id = local('git rev-parse HEAD', capture=True)
        _config_set(key='HEAD_COMMIT_ID', value=commit_id)


def build():
    # delete old dist folder
    local('cd static && npm run build')


# === DB ===
def migrate():
    if env.env == 'development':
        local('./manage.py migrate')
    else:

        if raw_input('\nDo you really want to MIGRATE DATABASE of \
            {heroku_app}? YES or [NO]: '.format(**env)) == 'YES':
            local('heroku run python manage.py migrate \
                --app {heroku_app}'.format(**env))
        else:
            print('\nMIGRATE DATABASE aborted')


# === Heroku ===
def ps():
    local('heroku ps --app {heroku_app}'.format(**env))


def restart():
    if raw_input('\nDo you really want to RESTART (web/worker) \
        {heroku_app}? YES or [NO]: '.format(**env)) == 'YES':
        local('heroku ps:restart web --app {heroku_app}'.format(**env))
    else:
        print('\nRESTART aborted')


def tail():
    local('heroku logs --tail --app {heroku_app}'.format(**env))


def shell():
    if env.env == 'development':
        local('./manage.py shell_plus --use-pythonrc')
    else:
        local('heroku run python manage.py shell \
              --app {heroku_app}'.format(**env))


def bash():
    local('heroku run bash --app {heroku_app}'.format(**env))


def config():
    local('heroku config --app {heroku_app}'.format(**env))


def _config_set(key=None, value=None):
    if key and value:
        local('heroku config:set {}={} \
            --app {heroku_app}'.format(key, value, **env))
    else:
        print('\nErr!')


def maintenance(mode='on'):
    local('heroku maintenance:{} --app {heroku_app}'.format(mode, **env))


# === Utils ===
def generatesecret():
    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    key = get_random_string(50, chars)
    print('key: {}'.format(key))
