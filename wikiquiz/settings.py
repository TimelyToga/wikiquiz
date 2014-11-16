"""
Django settings for wikiquiz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

## BIG DIRECTORIES
WEB_DIR = os.path.abspath(os.path.join(BASE_DIR, 'webfiles'))
TEMPLATE_DIRS = (os.path.abspath(os.path.join(WEB_DIR, 'templates')), )
STATIC_DIR = os.path.abspath(os.path.join(WEB_DIR, 'static'))

## LESSER DIRECTORIES
FAVICON = os.path.abspath(os.path.join(STATIC_DIR, 'favicon.ico'))
JS_DIR = os.path.abspath(os.path.join(STATIC_DIR, 'js'))
CSS_DIR = os.path.abspath(os.path.join(STATIC_DIR, 'css'))
IMG_DIR = os.path.abspath(os.path.join(STATIC_DIR, 'img'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6*rxudbv($15+p3i#epsm!1-%hb@z9fxg@_d$cwibd2r$&q+e7'

## READABILITY
PARSER_TOKEN = "559d23a43dfef9f3f7f398b93da5681aa519ee36"
WIKI_URL = "https://en.wikipedia.org/wiki/"
MIN_SENT_LENGTH = 60


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'wikiquiz.urls'

WSGI_APPLICATION = 'wikiquiz.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
