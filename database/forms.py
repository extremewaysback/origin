from django.forms import ModelForm,DateInput
from models import defectdata

class defectdataForm(ModelForm):
    class Meta:
        model=defectdata
        fields=['product','layer','lot','wafer','scantime','defectcount','remarks']
        #widgets={'scantime':DateInput}