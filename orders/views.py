#orders/views.py
from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
"""
import weasyprint
from io import BytesIO

@staff_member_required  #only staff member can access this view
def admin_order_pdf(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    html=render_to_string('orders/order/pdf.html',{'order':order}) #render the template and save in html
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='filename="order_{}.pdf"'.format(order.id) #specify the file name
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.css(settings.STATIC_ROOT+'css/pdf.css')])
    return response   
"""
    
def order_create(request):
    '''get the product in cart of session and generate an order'''
    cart=Cart(request)  #get the cart information as a dictionary
    if request.method=='POST':
        form=OrderCreateForm(request.POST) #get the user input information
        if form.is_valid():
            order=form.save()  #save the input information into database 
            for item in cart:  #save the products in cart into database
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            #clear the cart information in session
            cart.clear()
            #launch asynchronous task
            #order_created.delay(order.id)
            
            #set the order in the session    
            request.session['order_id']=order.id   
            #return render(request, 'orders/order/created.html',{'order':order})
            
            #redirect to the payment
            return redirect(reverse('payment:process'))
            
    else:
        form=OrderCreateForm()
    return render(request, 'orders/order/create.html',{'cart':cart,'form':form})
                

#Create a custom view to display informaiton about an order
@staff_member_required
def admin_order_detail(request, order_id):
    order=get_object_or_404(Order, id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order':order})
    
   
