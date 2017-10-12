from whitenoise.django import DjangoWhiteNoise

from config.wsgi import application as _application


application = DjangoWhiteNoise(_application)
