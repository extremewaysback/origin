#pro.py/settings
# Custom settings for the production environment

from .base import *

DEBUG=FALSE

ADMINS=(
    ('Ibelin G', 'extremewaysback@hotmail.com'),
    )
    
ALLOWED_HOSTS=['https://origint.herokuapp.com', 'origint.herokuapp.com']