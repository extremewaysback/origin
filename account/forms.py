#account/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('username','first_name','email')  #These fields will be validated based on their corresponding model fields.  
    #You can provide a clean_<fieldname>() method to any of your form fields in order to clean the value or raise form validation errors for the specific field.
    #This check is done when we validate the form calling its is_valid() method.
    #Forms also include a general clean() method to validate the entire form, whichis useful to validate fields that depend on each other.
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
        
class UserEditForm(forms.ModelForm):
    '''allow users to edit the first, last name and email which are stored in the built-in User model'''
    class Meta:
        model=User
        fields=('first_name','last_name','email')
        
class ProfileEditForm(forms.ModelForm):
    '''allow users to edit the extra data we save in the custom Profile model. Users will be able to edit their date of birth and upload a picture'''
    class Meta:
        model=Profile
        fields=('date_of_birth','photo')