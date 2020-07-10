"""
Django settings for zakat project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dwhkv)h1i)yx@p2t4a=vhh33jv1*vi7577exxwdv(tf*(1yzw9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# heroku
# ALLOWED_HOSTS = ['zakatkazan.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 3rd-party
    'channels',
    'django_countries',
    'graphene_django',
    'avatar',
    # our apps
    'accounts',
    'projects',
    'news',
    'payment',
    'partners',
    'dashboard',
    'dashboard.users',
    'dashboard.employee',
    'dashboard.partner',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zakat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'zakat.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'zakat',
        'CLIENT': {
            'host': os.getenv('DB_HOST', 'localhost'),
            # 'host': os.getenv('DB_HOST', ''),
            'port': int(os.getenv('DB_PORT', 27017)),
            'username': os.getenv('DB_USERNAME', ''),
            'password': os.getenv('DB_PASSWORD', ''),
            'authSource': 'admin',
        }
    }
}

GRAPHENE = {
    'SCHEMA': 'zakat.schema.schema'
}

# Register conversion rules from Djongo-specific fields
from graphene_django.converter import convert_django_field
from djongo.models import EmbeddedField, ArrayField


@convert_django_field.register(EmbeddedField)
def convert_embedded_field(field, registry=None):
    return field


@convert_django_field.register(ArrayField)
def convert_embedded_field(field, registry=None):
    return field


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AAUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

from PIL import Image

AVATAR_CACHE_ENABLED = False
AVATAR_DEFAULT_URL = '/dashboard/defaultAvatar.jpg'
AVATAR_DEFAULT_SIZE = 80
AVATAR_AUTO_GENERATE_SIZES = (80,)
AVATAR_MAX_AVATARS_PER_USER = 1
AVATAR_PROVIDERS = (
    'avatar.providers.PrimaryAvatarProvider',
    # 'avatar.providers.GravatarAvatarProvider',
    'avatar.providers.DefaultAvatarProvider',
)
AVATAR_GRAVATAR_DEFAULT = '/dashboard/defaultAvatar.jpg'
AVATAR_GRAVATAR_FORCEDEFAULT = False
AVATAR_GRAVATAR_FIELD = 'email'
AVATAR_GRAVATAR_BASE_URL = '/dashboard/defaultAvatar.jpg'
AVATAR_CHANGE_TEMPLATE = 'avatar/change.html'
AVATAR_ALLOWED_FILE_EXTS = ('.jpg', '.jpeg', '.png')
AVATAR_ADD_TEMPLATE = 'avatar/add.html'
AVATAR_MAX_SIZE = 1024 * 1024 * 2
AVATAR_STORAGE_DIR = 'avatars'
AVATAR_HASH_USERDIRNAMES = False
AVATAR_EXPOSE_USERNAMES = False
AVATAR_HASH_FILENAMES = False
AVATAR_THUMB_FORMAT = "png"
AVATAR_THUMB_QUALITY = 80
AVATAR_RESIZE_METHOD = Image.ANTIALIAS

# Конфигурация Channels
ASGI_APPLICATION = "zakat.routing.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [("127.0.0.1", 6379)],
            "symmetric_encryption_keys": [SECRET_KEY],
        },
    },
}

CELERY_BROKER_URL = os.getenv('BROKER_URL', '')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD', '')

# Activate Django-Heroku.
# django_heroku.settings(locals())
