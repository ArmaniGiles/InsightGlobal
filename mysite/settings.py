"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i%06y2q&4l-!nv*8oolv470b!o)!xg*^9f7^d=q10#b$wd%c_e'
# SECRET_KEY = os.environ.get('SECRET_KEY')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# export SECRET_KEY='847e44e26a02eee37a3ee0071629844b36c2ee273691d6a6'
# export DEBUG_VALUE="True"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# ALLOWED_HOSTS = ['ancient-meadow-75191.mysite.com']
# ALLOWED_HOSTS = ['ancient-meadow-75191.herokuapp.com']
# ALLOWED_HOSTS = ['0.0.0.0', 'localhost','bless727.herokuapp.com']
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1','bless727.herokuapp.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',

    'mysite.search',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mysite/templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }
#--log-file -
# DATABASES = {
#     'default': {

#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mysite',
#         'USER':'postgres',
#         'PASSWORD':'Sidewalk727',
#         'HOST':'bless727.herokuapp.com',
#         'PORT':'5432'

#     }
   
# }


DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
        'USER':'postgres',
        'PASSWORD':'Sidewalk727',
        'HOST':'127.0.0.1',
        'PORT':'5432'

    }
   
}

# DATABASES = {}
# DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, './mysite/static/')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, './mysite/static'),
# )
# django_heroku.settings(locals())
# prod_db  =  dj_database_url.config(default='postgres://fiutbcxoyxeuqe:f23b61665dd19170ad33a4357e8f6c9d42452ba6657b8430d459efa9e5f48ec0@ec2-107-20-167-241.compute-1.amazonaws.com:5432/d7cht05qse4g2i')
import dj_database_url 
prod_db  =  dj_database_url.config()
# print('prod_db ', prod_db)
DATABASES['default'].update(prod_db)
# del DATABASES['default']['OPTIONS']['sslmode']
# try to load local_settings.py if it exists
# try:
#   from local_settings import *
# except Exception as e:
#   pass