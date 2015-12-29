# blog/forms.py

from django import forms
from .models import Comment

# Create a form by inheriting the base Form class. We use different field types for Django
# to validate fields accrodingly.
class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False, widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment #indicate which model to use to build the form in the Meta class of the form.
        fields=('name','email','body') #Those are the only fields our users will be able to fill in
        #By default, django builds a form field for each field contained in the model. However, you can explicitly 
        #tell the framework which fields you exclude using an exclude list of fields.
        
            
class SearchForm(forms.Form):
    query=forms.CharField()    