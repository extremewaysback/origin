#account/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


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


def register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Create a new user object but avoid saving it yet
            new_user=user_form.save(commit=False)
            #Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])#Method of User that handles encryption to save for safety.
            #save the User object
            new_user.save()
            #Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user':new_user})
            
    else:
        user_form=UserRegistrationForm()
    return render(request,'account/register.html',{'user_form':user_form})
        
@login_required #login_required decorator because users have to be authenticated to edit their profile
def edit(request):
    flag=False
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        try:
            instance=request.user.profile
        except:
            instance=None
        profile_form=ProfileEditForm(instance=instance,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            #profile_form.save()
            profile_form.save(commit=False)
            profile_form.instance.user=user_form.instance
            profile_form.instance.save()
            flag=True
    else:
        user_form=UserEditForm(instance=request.user)
        try:
            instance=request.user.profile
        except:
            instance=None
        profile_form=ProfileEditForm(instance=instance)
        
    return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form,'flag':flag})
