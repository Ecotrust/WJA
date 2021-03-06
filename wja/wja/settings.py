"""
Django settings for wja project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*y*-+ufz%3z29yu468-ojg*&^or82*rn@if*gpga%krz&v9i)5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'wja/templates')
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'ui'
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

ROOT_URLCONF = 'wja.urls'

WSGI_APPLICATION = 'wja.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'wja', 'db.sqlite3'),
    }
}


GEOMETRY_DB_SRID = 3857


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'wja', 'static')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

SERVER_SRID = 4326

GEOJSON_SRID = 4326

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

HEADER_LOOKUP = {
    'Unique ID': 'unique_id',
    'Data Source': 'data_source',
    'Project Name': 'project_name',
    'Ownership': 'ownership',
    'Access': 'access',
    'Expected or Completed Treatment Date': 'treatment_date',
    'Treatment Type': 'treatment_type',
    'Treated Acres': 'treated_acres',
    'Average Slope': 'average_slope',
    'Current Status': 'current_status',
    'Tree Species': 'tree_species',
    'Juniper Phase': 'juniper_phase',
    'Average DBH': 'average_dbh',
    'Tons/Acre': 'tons_per_acre',
    'Latitude': 'latitude',
    'Longitude': 'longitude',
    'Contact Name': 'contact_name',
    'Contact Email': 'contact_email',
    'Contact Phone': 'contact_phone'
}

HEADER_REVERSE_LOOKUP = {}
for key in HEADER_LOOKUP.keys():
    value = HEADER_LOOKUP[key]
    HEADER_REVERSE_LOOKUP[value] = key

try:
    from .local_settings import *
except ImportError:
    pass
