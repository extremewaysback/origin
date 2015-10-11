#subscription/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Subscribers
from forms import SubscribersForm
# Create your views here.


def subscription(request):
    if request.method=='POST':
        form=SubscribersForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            s=Subscribers.objects.create(email=cd['email'],password=cd['password'])
            return HttpResponseRedirect('/subscription/success/',{'s':s})
    else:
        form=SubscribersForm()
    return render(request,'subscription/subscription.html',{'form':form})
    
    
def success(request):
    return render(request,'subscription/success.html')  