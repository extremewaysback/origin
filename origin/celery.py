#celery.py for shop app
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

#set the default django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','origin.settings')

app=Celery('shop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
