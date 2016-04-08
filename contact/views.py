# /contact/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from contact.forms import ContactItemForm   #import forms into views
from contact.models import ContactItem 
import smtplib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
#contact_form has the attributes of ===subject & email & message

def thanks(request):
    return render(request,'contact/thanks.html')

def contact(request):
    if request.method == 'POST':
        form = ContactItemForm(request.POST) #pass the request data to get a form 
        if form.is_valid():              #validate the 
            cd = form.cleaned_data
            
            #send a mail
            to = 'extremewaysback@hotmail.com'
            gmail_user = 'extremeways@126.com'
            gmail_pwd = 'II68738050'
            smtpserver = smtplib.SMTP("smtp.126.com",25)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(gmail_user, gmail_pwd)
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:'+cd['subject']+ '\n'
            msg = header + '\n'+ cd['message']+'\n\n'
            smtpserver.sendmail(gmail_user, to, msg)
            smtpserver.close()
            
            '''
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'extremeways@126.com'),
                ['extremewaysback@hotmail.com'],
                     )
            '''
            ContactItem(cd['subject'],cd['message'],cd.get('email','noreply@example.com'))
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactItemForm(
            initial={'subject': '','email':''}
        )
    return render(request, 'contact/contact_form.html', {'form': form})   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    