# coding:utf-8
"""
Django settings for shopsys project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_DIR = os.path.dirname(__file__)  # 设置templtes路径
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#4b9qo#n#pddyja5)xbcm0)))bfp3b46db4vma7b)eppz80^ki'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shopsys.apps.catalog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'shopsys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SETTINGS_DIR, 'templates'),
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

WSGI_APPLICATION = 'shopsys.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'shopsys',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '123456',
        # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'OPTIONS': {
            "init_command": "SET default_storage_engine=MyISAM",
        },
        'HOST': '127.0.0.1',
        'PORT': '3306',  # Set to empty string for default.
        'TEST': {},
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
DATE_FORMAT = 'Y-m-d'
TIME_ZONE = 'Asia/Shanghai'

# 是否开启国际化，不开启时可以不加载翻译模块优化性能
USE_I18N = False

# 本地化格式支持，为True使用系统licale设置显示数字，时间等格式
USE_L10N = True

USE_TZ = True

# 是否设置Etag,设置etag可以降低网络资源开销，但会增加服务器性能开销
USE_ETAGS = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
