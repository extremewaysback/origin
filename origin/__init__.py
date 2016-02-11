# Import celery module in the __init__.py file of to make sure it is loaded when
# django starts

from .celery import app as celery_app # Now can start programming asynchronous tasks for your applicaitons.