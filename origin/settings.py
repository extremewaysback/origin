"""
Django settings for origin project.

Generated by 'django-admin startproject' using Django 1.8.3.

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
SECRET_KEY = 'j^%32111th*jd#&h&=z__i6x+h(@2d2_c&ie^^k*7xyp#@&96$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []   #is not applied while debug mode is on or when running tests.
#Once you are going to move your site to production and set DEBUG to False, you
#will have to add your domain/host to this setting in order to allow it to serve the Django site.


# Application definition

INSTALLED_APPS = (
    'account',
    'django.contrib.admin',#this is an administration site
    'django.contrib.auth',#this is an authentication framework
    'django.contrib.contenttypes',#track all of the models installed in the project
    'django.contrib.sessions',#this is a session framework, database-backed sessions
    'django.contrib.messages',#this is a messaging framework
    'django.contrib.staticfiles', #this is a framework for managing static files
    'contact',
    #'subscription',
    'database',
    #'polls',
    'blog',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'haystack',#search enginer
    'shop',
    'cart',
    'orders',
)


SITE_ID=3

# Define the search engine backends for haystack
'''
HAYSTACK_CONNECTIONS={
    'default':{
        'ENGINE':'haystack.backends.solr_backend.SolrEngine',
        'URL':'http://127.0.0.1:8983/solr/blog'
        },
}
'''

#The simple backend using very basic matching via the database itself. It's not recommended for production use but it will return results
HAYSTACK_CONNECTIONS={
                    'default':{
                               'ENGINE':'haystack.backends.simple_backend.SimpleEngine',
                              },
                     }
                   

#setting for dashboard login
from django.core.urlresolvers import reverse_lazy
LOGIN_REDIRECT_URL=reverse_lazy('dashboard')#tells django which url to redirect after login, if the contrib.auth.views.login view gets no next parameter
LOGIN_URL=reverse_lazy('login')#is the url to redirect the user to log in
LOGOUT_URL=reverse_lazy('logout')#is the url to redirect the user to log out



#MIDDLEWARE_CLASSES is a tuple containing middlewares to be executed.

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware', #every request get a session attribute like a dictionary
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

#This is the key that we are going to use to store the cart in the user session
#Since Django sessions are per-visitor, we can use the same cart session key for all sessions
CART_SESSION_ID='cart'

ROOT_URLCONF = 'origin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'origin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddk5c3r8jv6eao',
        'USER':'wtzvndsrnapvjl',
        'PASSWORD':'83n2AdqUEEAGjBmhIHQ8-Cfh0X',
        'HOST':'ec2-107-21-221-107.compute-1.amazonaws.com',
        'PORT':'5432',
    }
}


#Add an SMTP configuration, so that django is able to send e-mails.
#Can configure Django to write e-mails to the standard output instead of sending them through an SMTP server.
#Django provides an e-mail backend to write e-mails to the console.
#The EMAIL_BACKEND setting indicates the class to use to send e-mails
#During developing
#EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'




# Giving the email parameters for default mail
EMAIL_HOST='smtp.126.com'
EMAIL_PORT=25
EMAIL_HOST_USER='extremeways@126.com'
EMAIL_HOST_PASSWORD='II68738050'
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL='extremeways@126.com'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(
   os.path.join(BASE_DIR, "static"),
                  )
STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT='staticfiles'

#serve media files uploaded by users with the development server

MEDIA_URL='/media/'#the base URL to serve the media files uploaded by users
MEDIA_ROOT=os.path.join(BASE_DIR,'media/')#build the path dynamically relative to our project path to make our code more generic
