"""Production settings and globals."""

from __future__ import absolute_import
import os
import environ

env_file = str((environ.Path(__file__) - 4).path('.env.prod'))
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

from .base import *

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS + EXTENSION_APPS
########## END APP CONFIGURATION

########## SECRET CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('SECRET_KEY')
########## END SECRET CONFIGURATION



########## TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
########## END TEMPLATE CONFIGURATION

# MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',) + MIDDLEWARE_CLASSES
# MIDDLEWARE_CLASSES += ('django.middleware.cache.FetchFromCacheMiddleware',)

# https://docs.djangoproject.com/en/dev/ref/middleware/#django.middleware.common.BrokenLinkEmailsMiddleware
MIDDLEWARE += ('django.middleware.common.BrokenLinkEmailsMiddleware',)
