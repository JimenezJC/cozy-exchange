"""
Django settings for django_config project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import datetime
import dj_database_url
import os
import environ

base = environ.Path(__file__) - 3
env = environ.Env()
environ.Env.read_env(env_file=base('.env'))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APPS_DIR = os.path.join(BASE_DIR, 'apps')



# SECRET KEY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-SECRET_KEY
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('SECRET_KEY')


# DEBUG
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = env('DEBUG')


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#admins
# https://docs.djangoproject.com/en/1.10/ref/settings/#managers

ADMINS = (
    ("""Michael A. Gonzalez""", 'GonzalezMA.CHOP@gmail.com'),
)

MANAGERS = ADMINS


# APP CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#installed-apps

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'webpack_loader',
    'corsheaders'
]

LOCAL_APPS = [
    'apps.store',
    'apps.contact',
    'apps.profiles',
    'apps.comments',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/topics/http/middleware/

DJANGO_SECURITY_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]

DJANGO_MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE = DJANGO_SECURITY_MIDDLEWARE + DJANGO_MIDDLEWARE

CORS_ORIGIN_WHITELIST = (
    '0.0.0.0:3000',
)

# URL Configuration
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#root-urlconf

ROOT_URLCONF = 'config.urls'


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/topics/templates/

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APPS_DIR, 'templates')],
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


# WGSI CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#wsgi-application

WSGI_APPLICATION = 'config.wsgi.application'


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL')),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Added this to support deployment on Heroku
# https://devcenter.heroku.com/articles/django-app-configuration
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
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


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#media-root
# https://docs.djangoproject.com/en/1.10/ref/settings/#media-url

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Django REST framework
# ------------------------------------------------------------------------------
# http://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),

}


# Django REST-AUTH framework
# ------------------------------------------------------------------------------
# https://github.com/Tivix/django-rest-auth/
# https://github.com/GetBlimp/django-rest-framework-jwt

REST_USE_JWT = True

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    'JWT_ALLOW_REFRESH': True,
}

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/topics/email/

EMAIL_PORT = env('EMAIL_PORT')

EMAIL_HOST = env('EMAIL_HOST')

EMAIL_BACKEND = env('EMAIL_BACKEND')

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
