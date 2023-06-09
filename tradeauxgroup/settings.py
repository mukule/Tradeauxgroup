"""
Django settings for tradeauxgroup project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=$iq_s#(@nhqw-1l7qz_*2tgacpvcwrw6id77g@^_j5p$6(97y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'crispy_forms',
    'crispy_bootstrap4',
    'tenders',
    'phonenumbers',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tradeauxgroup.urls'

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

WSGI_APPLICATION = 'tradeauxgroup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'soft01v_tradeaux',
        'USER': 'soft01v_neslon',
        'PASSWORD': '3T39v8Idtd26',
        'HOST': 'localhost',
        'PORT': '2700',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True
env = environ.Env(DEBUG=(bool, False))
# reading .env file
environ.Env.read_env()


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'tenders:index'
LOGOUT_REDIRECT_URL = 'login'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

consumer_key = "piumJBdCtSxo6GX9p8j8kqcljVJNXJMA"
consumer_secret = "pd7cx9QgbZReJdZ1"

LOGGING = {
		'version': 1,
		'disable_existing_loggers': False,
		'formatters': {
			'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
			},
			'simple': {
			'format': '%(levelname)s %(message)s'
			},
		},
		'filters': {
			'require_debug_true': {
				'()': 'django.utils.log.RequireDebugTrue',
			},
		},
		'handlers': {
			'file': {
				'level': 'DEBUG',
				# 'class': 'logging.FileHandler',
				# 'filename': os.path.join(BASE_DIR,'storage/debug.log'),
				'class' : 'logging.handlers.TimedRotatingFileHandler',
				'filename' : os.path.join(BASE_DIR,'debug.log'),
				'when' : 'midnight',
				'interval' : 1,
				'backupCount': 0
			},
			'mail_admins': {
				'level': 'ERROR',
				'class': 'django.utils.log.AdminEmailHandler'
			},
			'console': {
				'level': 'DEBUG',
				'class': 'logging.StreamHandler',
			},
		},
		'loggers': {
			'django': {
				'handlers': ['file','mail_admins'],
				'level': 'ERROR',
				'propagate': False,
			},
			'django.request': {
				'handlers': ['file','mail_admins'],
				'level': 'ERROR',
				'propagate': False,
			},
			'django.db.backends': {
				'handlers': ['file'],
				'level': 'ERROR',
			},
			'xscape': {
				'handlers': ['file',*['console']*DEBUG],
				'level': 'DEBUG',
			},
		},
	}
