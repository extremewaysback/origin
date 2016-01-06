#account/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def user_login(request):
    if request.method=='POST':#if a POST method
        form=LoginForm(request.POST)#Instantiate the form with the submitted data with form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])#If the data is valid, authenticate the user against the database with authenticate() method
            if user is not None:#authenticate return a user object or None
                if user.is_active:#check the account is active or not
                    login(request,user)#If teh user is active, we login the website. Set the user in the session by calling the login() method and return a success message.
                    return render(request,'account/dashboard.html')
                else:
                    return HttpResponse('Disabled account')#the account is not active
            else:
                return HttpResponse('Invalid login')
    else:
        form=LoginForm()#if a GET request, we instantiate a new log in form with form=LoginForm()
    return render(request,'registration/login.html',{'form':form})


def user_logout(request):
    logout(request)
    return render(request,'account/logged_out.html')
                   
                              
                                             
                                                                           
#decorate view with the login_required decorator of the authentication framework
#The login_required decorator checks if the current user is authenticated
#If the user is authenticated, it executes the decorated view; if the user is not authenticated,
#it redirect to the login URL with the URL trying to access as a GET parameter named next.               
@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{"section":"dashboard"})#section track which section of the site the user is watching
       


