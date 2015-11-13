#CpMap ModelForm
from django.forms import ModelForm
from models import cpdata

class cpdataForm(ModelForm):
    class Meta:
        model=cpdata
        fields=['x','y','c','f']