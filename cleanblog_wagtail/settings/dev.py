from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_dlv1x$l#9f^os^p6__w0y8vuhtb@8advm*w(ij6gqwv6bsiur"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    "cleanblog.pythonanywhere.com",
    "www.cleanblog.pythonanywhere.com",
    'free-camel-deadly.ngrok-free.app',
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
