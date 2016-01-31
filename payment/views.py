#payment/views.py
from django.shortcuts import render,get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt

def payment_process(request):
    '''genertate the paypal form for the buy now button'''
    order_id=request.session.get('order_id') #get the current order from session or return None
    order=get_object_or_404(Order,id=order_id) #get the order object through order_id
    host=request.get_host()  #return the originating host of the request
       
    paypal_dict={
        'business':settings.PAYPAL_RECEIVER_EMAIL, #PayPal merchant account to process the payment
        'amount':'%.2f' % Decimal(str(order.get_total_cost())).quantize(Decimal('.01')), #the total amount to charge with precision to 0.01
        'item_name':'Order {}'.format(order.id),
        'invoice':str(order.id),
        'currency_code':'USD',
        'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url':'http://{}{}'.format(host,reverse('payment:done')),
        'cancel_return':'http://{}{}'.format(host,reverse('payment:canceled')),
        }
    
    form=PayPalPaymentsForm(initial=paypal_dict) #generate a custom PayPal's Buy now button to pay an order
    return render(request,'payment/process.html',{'order':order,'form':form})


@csrf_exempt #This decorator marks a view as being exempt from the protection ensured by the middleware
def payment_done(request):
    return render(request,'payment/done.html')
    
@csrf_exempt #to avoid django expecting a CSRF token
def payment_canceled(request):
    return render(request,'payment/canceled.html')