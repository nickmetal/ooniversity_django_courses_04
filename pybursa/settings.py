# encoding: utf-8

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

USE_DEFAULT_DB = 0 #MY settings item for local_settings
                   #using sqlite3(1) or postgres (0)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aty3&#t@$fq7&b8tl2(9ynuif7q3zgd1l*)=g_a=42y+^5b$7*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
USE_DEFAULT_DB = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'quadratic',
    'courses',
    'students',
    'coaches',
    'feedbacks',
    'sendgrid',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.template.context_processors.request',
# )

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

USE_I18N = True

USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
LOGIN_URL = "/login/"
STATIC_URL = '/static/'
STATICFILES_DIRS = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
# TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
       os.path.join(BASE_DIR, 'templates')
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
            # list if you haven't customized them:
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.request',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
        ],
    },

},
]


ADMINS = (('My','nickmetal92@gmail.com'),)

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_USE_TLS = False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
            },
        },
    'handlers': {
        'courses_logger': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            'formatter': 'simple',
        },
        'students_logger': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'courses': {
            'handlers': ['courses_logger'],
            'level': 'DEBUG',
        },
        'students': {
            'handlers': ['students_logger'],
            'level': 'WARNING',
        },
    },
}

try:
    from local_settings import *
    print "----> local_set-s(for DEPLOYED serv) is used now!"
except ImportError:
    print "----> local_settings not found! Localhost is used now"
