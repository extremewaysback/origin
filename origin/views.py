from django.shortcuts import render
from django.http import HttpResponseRedirect


def origin(request):
    return render(request,"origin/origin.html")
    
    
def experice(request):
    return render(request,"origin/experience.html")