#account/forms.py

from django import forms
from django.contrib.auth.models import User


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