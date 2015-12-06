#CpMap ModelForm
from django.forms import ModelForm
from models import cpdata

class cpdataForm(ModelForm):
    class Meta:
        model=cpdata
        fields=['x','y','c','f']
        
from django import forms

class UploadFileForm(forms.Form):
    '''A form to upload file'''
    title=forms.CharField(max_length=50)
    file=forms.FileField()
    
    