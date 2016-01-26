#import celery module in the __init__.py file of to make sure it is loaded when
#django starts

from .celery import app as celer_app