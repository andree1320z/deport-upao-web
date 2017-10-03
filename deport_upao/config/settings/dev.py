"""Development settings and globals."""

from __future__ import absolute_import
import os
import environ

environ.Env.read_env(str((environ.Path(__file__) - 4).path('.env')))

env_file = str((environ.Path(__file__) - 4).path('.env.dev'))
if os.path.exists(env_file):
    environ.Env.read_env(env_file)



from .base import *

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS + EXTENSION_APPS
########## END APP CONFIGURATION

########## DEBUG CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', default=True)
########## END DEBUG CONFIGURATION


########## TOOLBAR CONFIGURATION
# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION


########## SSL SERVER CONFIGURATION
# https://github.com/teddziuba/django-sslserver#getting-started
INSTALLED_APPS += (
    'sslserver',
)
########## END SSL SERVER CONFIGURATION