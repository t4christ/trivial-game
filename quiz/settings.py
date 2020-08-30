"""
Django settings for quiz project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)




#Environment variables
import dotenv
from dotenv import load_dotenv
dotenv.load_dotenv()
load_dotenv(os.path.join(BASE_DIR, '.env'))


SECRET_KEY = 'sm@g)(fbwdh5wc*xe@j++m9rh^uza5se9a57c5ptwkg*b@ki0x'

ALLOWED_HOSTS = ['*']
  
# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    # 'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party
    'crispy_forms',
    'storages',
    'gunicorn',


    # local apps
    'django_celery_beat',
    'django_celery_results',
    'erc',
    'recharge',    
]



# SITE_ID= 1




ERC_USER = os.environ.get('ERC_USER')
ERC_PASS = os.environ.get('ERC_PASS')
ERC_LOGIN_URL = 'https://clients.primeairtime.com/api/auth'
ERC_TOPUP_INFO = 'https://clients.primeairtime.com/api/topup/info/%(msisdn)s'
ERC_TOPUP_URL = 'https://clients.primeairtime.com/api/topup/exec/%(msisdn)s'

COUNTRY_CODE = 'NG'









AUTH_USER_MODEL = 'accounts.MyUser'


CRISPY_TEMPLATE_PACK = 'bootstrap3'

# MIDDLEWARE_CLASSES = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


LOGIN_URL = "/login/"
ROOT_URLCONF = 'quiz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'quiz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if  DEBUG:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gist',
        'USER': 'temitayo',
        'PASSWORD': 'gistpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


    # DATABASES = {'default': dj_database_url.config(default='postgres://temitayo:gistpassword@localhost/gist')}



    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME':  os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }
else:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DATABASE'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}






    # STATIC_URL = os.environ['STATIC_URL']
    # STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'STATIC-BUCKET-NAME')
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True



if DEBUG:
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
else:  
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE



CELERY_BEAT_SCHEDULE = {

'airtime': {
        'task': 'recharge_airtime',
        'schedule': 120.0,
        # 'args': (16, 16)
    },

    'remove_airtime': {
        'task': 'delete_airtime',
        'schedule': 240.0,
        # 'args': (16, 16)
    },




'airtime_level': {
        'task': 'recharge_airtime_level',
        'schedule': 90.0,
        # 'args': (16, 16)
    },


    'remove_airtime_level': {
        'task': 'delete_airtime_level',
        'schedule': 110.0,
        # 'args': (16, 16)
    }
}



# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.join(BASE_DIR, 'secure-media-eb1f179c0076.json')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

if DEBUG:

    STATIC_DIR = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
    STATIC_DIR,
    ]
    PROFILE_URL='profile_photo'
    MEDIA_URL = "media/"
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")


else:

    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3BotoStorage'
    PROFILE_URL='profile_photo'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
        }
    AWS_LOCATION = 'static'
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ]
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'









if DEBUG:
     EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
     EMAIL_FILE_PATH = os.path.join(BASE_DIR, '.emails')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.mailgun.org'
    EMAIL_PORT = 2525
    EMAIL_HOST_USER = os.getenv('EMAIL_USERNAME')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
    EMAIL_TIMEOUT = 30
    EMAIL_USE_TLS = False

