#payment/signals.py

from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order

def payment_notification(sender, **kwargs):
    ipn_obj=sender #an instance of PayPalIPN model 
    if ipn_obj.payment_status==ST_PP_COMPLETED:
        #payment was successful
        order=get_object_or_404(Order, id=ipn_obj.invoice)
        #mark the order as paid
        order.paid=True #modify the order object and save to database
        order.save()

valid_ipn_received.connect(payment_notification)
#have to make sure that signals models is loaded so that the receiver function is called when the valid_ipn_received signal
#is triggered.
#The best practice is to load your signals when the application containing them is loaded