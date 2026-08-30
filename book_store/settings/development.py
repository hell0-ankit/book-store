from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "10.71.222.149", #ip
    "localhost",
    "127.0.0.1",
]

# Local Database (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Local Email Backend 
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"