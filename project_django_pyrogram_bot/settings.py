from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-d9efu82#^7)$54*nl4xj^y7zf(e3w9&jv_m-d6zspv))ue!ung"

DEBUG = True
import os
ALLOWED_HOSTS = ["*"]

# Pyrogram BOT Settings
PYROGRAM_BOT = {
    "BOT_NAME": "app",
    "API_ID": "2650655",
    "API_HASH": "2318544e6bdb874d8503d21c2d1d2e94",
    "NOTIFY_STARTUP_ADMINS": True,
    "NOTIFY_SHUTDOWN_ADMIN": True,
}

# Application definition

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "treebeard",
    "accounts",
    "decision",
    "bot.apps.BotConfig",
    'import_export',
    'django_cleanup.apps.CleanupConfig',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project_django_pyrogram_bot.urls"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project_django_pyrogram_bot.wsgi.application"
AUTH_USER_MODEL = "accounts.User"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'value',
        'USER': 'abdallh',
        'PASSWORD': 'thepassword',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    #         },
    # {
    #         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    #         },
    # {
    #         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    #         },
    # {
    #         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    #         },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ar-iq"

TIME_ZONE = "UTC"

USE_I18N = True
LOGOUT_REDIRECT_URL = 'login'
USE_TZ = True
DEFAULT_CHARSET = 'utf-8'
# LOGIN_REDIRECT_URL = ""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# LOGIN_REDIRECT_URL = '/app/'


# https://github.com/django/django/blob/main/django/utils/log.py
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "medium": {
            "format": "[{module}]: {levelname} {asctime} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "console-medium": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "medium",
        },
        "console-verbose": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file-medium": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/".join([f"{BASE_DIR.as_posix()}", "pyrogram_bot.log"]),
            "formatter": "medium",
        },
        "file-verbose": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/".join([f"{BASE_DIR.as_posix()}", "pyrogram_bot.log"]),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "root": {
            "handlers": ["console-medium", "file-medium"],
            "level": "DEBUG",
        },
        "pyrogram.session.session": {
            "handlers": ["console-medium", "file-medium"],
            "level": "WARNING",
        },
    },
}

# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
