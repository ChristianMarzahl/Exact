"""
Django settings for imagetagger project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'imagetagger.annotations',
    'imagetagger.base',
    'imagetagger.images',
    'imagetagger.users',
    'imagetagger.tools',
    'imagetagger.administration',
    'django.contrib.admin',
    'imagetagger.tagger_messages',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'widget_tweaks',
    'friendlytagloader',
    'plugins',
    'util',
    'django_registration'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'imagetagger.urls'


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
                'imagetagger.base.context_processors.base_data',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'imagetagger.wsgi.application'

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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

AUTH_USER_MODEL = 'users.User'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'  # Timezone of your server

USE_I18N = True

USE_L10N = True

USE_TZ = False

PROBLEMS_URL = 'https://github.com/ChristianMarzahl/imagetagger/issues'
PROBLEMS_TEXT = ''

LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/images/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.INFO: 'info',
    messages.ERROR: 'danger',
    messages.WARNING: 'warning',
    messages.SUCCESS: 'success',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

EXPORT_SEPARATOR = '|'
DATA_PATH = os.path.join(BASE_DIR, 'data')

IMAGE_PATH = os.path.join(BASE_DIR, 'images')  # the absolute path to the folder with the imagesets

MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
MEDIA_URL= "/media/"

# filename extension of accepted imagefiles
IMAGE_EXTENSION = {
    'png',
    'jpeg',
}

# Sets the default expire time for new messages in days
DEFAULT_EXPIRE_TIME = 7

# Sets the default number of messages per page
MESSAGES_PER_PAGE = 10
