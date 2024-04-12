"""
Django settings for recipe_site project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from dotenv import load_dotenv 
import os
from pathlib import Path


load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-d&g+l=si64+@diirn&io^f=fxrz+a$3mwc!k5zt$xhhvm-%ms2'
SECRET_KEY = os.getenv('SECRET_KEY')
# DEBUG = bool(os.environ.get('DEBUG'))
if os.environ.get("DEBUG") == "False":
    DEBUG = False
else:
    DEBUG = True
CSRF_TRUSTED_ORIGINS = []
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
SESSION_COOKIE_SECURE = True 
CSRF_COOKIE_SECURE = True
ALLOWED_HOSTS = ["127.0.0.1", 
                "culinarywebsite.pythonanywhere.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recipe_site_app',
    "users.apps.UsersConfig",
    
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

ROOT_URLCONF = 'recipe_site.urls'

TEMPLATES = [
    {
        
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'recipe_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DBNAME"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("MYSQL_HOST"),
        "OPTIONS": {
            "init_command": "SET NAMES 'utf8mb4';SET sql_mode = 'STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'ctatic/'
STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static')
    # LOGIN_URL
    # LOGOUT_REDIRECT_URL = 'recipe_site_app:index'

    # LOGOUT_REDIRECT_URL = 'recipe_site_app:index'

]
# Default primary key field type'
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'