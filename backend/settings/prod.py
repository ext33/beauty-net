from .dev import *

############
# DATABASE #
############

DATABASES = {
    # db settings
}

############
# SECURITY #
############

DEBUG = False
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

# Set to your Domain here
ALLOWED_HOSTS = ['*']

# CORS settings
# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#
# )
