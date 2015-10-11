# subscription/forms.py

from django.forms import ModelForm,PasswordInput
from models import Subscribers

class SubscribersForm(ModelForm):
    class Meta:
        model=Subscribers
        fields=['email','password']
        widgets={'password':PasswordInput}

