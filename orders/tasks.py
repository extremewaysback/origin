# orders/tasks.py for celery to launch asynchronous tasks
# This is the place where Celery will look for asynchronous tasks

from celery import task
from django.core.mail import send_mail
from .models import Order

#A celery task is just a python function decored with task.

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order=Order.objects.get(id=order_id)
    subject='Order nr. {}'.format(order.id)
    message='Dear {},\n\nYou have successfully places an order. Your order id is {}.'.format(order.first_name,order.id)
    mail_sent=send_mail(subject,message,'extremeways@126.com',[str(order.email)], fail_silently=False)
    return mail_sent