"""
Django settings for ims_site project.
Generated by 'django-admin startproject' using Django 1.8.2.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'or15=#(l_09rl#k3-$%b^r@s6eqx@!_n1m+$o1ni-rt&pxd-4@'
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
    'django.contrib.sites',
    'jqchat',
    'faculty',
    'students',
    'registration',
    'general',
    'multiform',
    # 'django_filters',
    # 'south',
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
ROOT_URLCONF = 'ims_site.urls'
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
# TEMPLATE_DIRS = ('/home/user/Documents/ims_site-jqchat/templates/',) #this is defined in old style to support the jqchat app
WSGI_APPLICATION = 'ims_site.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
'/var/www/static/',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
#Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home2/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a # trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
# to solve csrf token missing error on admin page
SESSION_COOKIE_SECURE = False
SITE_ID = 1
# SOUTH_DATABASE_ADAPTERS = {
# 'default': "south.db.sqlite3"
# }
# Registration app settings
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window;
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
# REGISTRATION_DEFAULT_FROM_EMAIL = 'Conformation for IMS - Executives registration'#Optional. If set, emails sent through the registration app will use this string. Falls back to using Django's built-in DEFAULT_FROM_EMAIL setting.
REGISTRATION_EMAIL_HTML = True#Optional. If this is False, registration emails will be send in plain text. If this is True, emails will be sent as HTML. Defaults to True
# Email setup
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ims.executives@gmail.com'
EMAIL_HOST_PASSWORD = 'tioiragynmihkrwn' #for appname 'iloveindia'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'ims.executives@gmail.com'
DEFAULT_TO_EMAIL = 'to email'
LOGIN_REDIRECT_URL = '/accounts/auth/'

# AUTHENTICATION_BACKENDS = ('registration.backends.default.backend.EmailAuthBackend',)










# """
# Django settings for ims_site project.

# Generated by 'django-admin startproject' using Django 1.8.2.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.8/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.8/ref/settings/
# """

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'or15=#(l_09rl#k3-$%b^r@s6eqx@!_n1m+$o1ni-rt&pxd-4@'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# # Application definition

# INSTALLED_APPS = (
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django.contrib.sites',
#     'jqchat',
#     'faculty',
#     'students',
#     'general',
#     'registration',
#     'multiform',
    
    
    
#     # 'south',
    
# )

# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
    
# )

# ROOT_URLCONF = 'ims_site.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
# # TEMPLATE_DIRS = ('/home/user/Documents/ims_site-jqchat/templates/',) #this is defined in old style to support the jqchat app

# WSGI_APPLICATION = 'ims_site.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# # Internationalization
# # https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
#     '/var/www/static/',
# )

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.8/howto/static-files/
# STATIC_URL = '/static/'

# #Absolute filesystem path to the directory that will hold user-uploaded files.
# # Example: "/home2/media/media.lawrence.com/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# # URL that handles the media served from MEDIA_ROOT. Make sure to use a # trailing slash. 
# # Examples: "http://media.lawrence.com/media/", "http://example.com/media/" 
# MEDIA_URL = '/media/'

# # to solve csrf token missing error on admin page

# SESSION_COOKIE_SECURE = False
# SITE_ID = 1

# # SOUTH_DATABASE_ADAPTERS = {
# #     'default': "south.db.sqlite3"
# # }

# # Registration app settings
# ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; 
# REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
# REGISTRATION_DEFAULT_FROM_EMAIL = 'Conformation for IMS - Executives registration'#Optional. If set, emails sent through the registration app will use this string. Falls back to using Django's built-in DEFAULT_FROM_EMAIL setting.
# REGISTRATION_EMAIL_HTML = True#Optional. If this is False, registration emails will be send in plain text. If this is True, emails will be sent as HTML. Defaults to True
# # Email setup
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'ims.executives@gmail.com'
# EMAIL_HOST_PASSWORD = 'tioiragynmihkrwn' #for appname 'iloveindia'
# EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = 'ims.executives@gmail.com'
# # DEFAULT_TO_EMAIL = 'to email'

# LOGIN_REDIRECT_URL = '/accounts/auth/'

