#origin/celery.py
#create a new proj/proj/celery.py module that defines the Celery instance
#Provide a configuration for the Celery instance.

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

#set the default django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','origin.settings')

app=Celery('origin') #create an instance for the origin project

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #Celery will look for a tasks.py file in each application to load asynchronous tasks defined in it.
