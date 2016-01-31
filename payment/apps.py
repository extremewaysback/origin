#payment/apps.py
from django.apps import AppConfig

class PaymentConfig(AppConfig):
    '''a custom AppConfig class for the payment application'''
    name='payment' #the name of the application
    verbose_name='Payment' #human-readble format
    
    def ready(self):
        '''make sure signals.py are loaded when the application is initialized'''
        #import signal handlers
        import payment.signals