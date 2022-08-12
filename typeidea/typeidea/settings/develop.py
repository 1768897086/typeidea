from .base import * # NOQA


DEBUG = True

DATABASES = {
    'default': 'django.db.backends.sqlit3',
    'NAME': os.path.jion(BASE_DIR, 'db.sqlite3')
}