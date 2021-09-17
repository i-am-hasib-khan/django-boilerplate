from decouple import config

from django_boilerplate.settings.base_settings import *

env = config("ENVIRONMENT")

if env == "DEV":
    from django_boilerplate.settings.dev_settings import *
elif env == "PROD":
    from django_boilerplate.settings.prod_settings import *
