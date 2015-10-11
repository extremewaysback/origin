# /contact/forms.py

#The primary way to use the forms framework is to define a Form class for each HTML <form>
#you're dealing with.

#Create a forms.py file in the same directory as your views.py

#This is pretty intuitive, and it's similar to django's model syntax. Each field
#in the form is represented by a type of Field class---CharField and EmailField
# are the ony types of fields used here---as attributes of a Form class.

from django.forms import ModelForm, Textarea
from models import ContactItem

#define the main input boxes of the HTML<form>
#just the contect of the table of list without

class ContactItemForm(ModelForm):
    class Meta:
        model=ContactItem
        fields=['subject','email','message']
        widgets={'message':Textarea}
