DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '{{ dbname }}',
        'USER': '{{ dbname }}',
        'PASSWORD': '{{ dbname }}',
        'HOST':'localhost',
    }
}

DEBUG = {{ debug }}
TEMPLATE_DEBUG = {{ debug }} 

ADMINS = (('Ryan Hodges', 'rhodges@ecotrust.org'),)
ALLOWED_HOSTS = ['{{allowed_host}}']

SECRET_KEY = '{{ secretkey }}'
