from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import defectdata
from forms import defectdataForm
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def register(request):
    if request.method=='POST':
        form=defectdataForm(request.POST) #interface with html
        if form.is_valid():
            cd=form.cleaned_data
            #if cd not in Student.objects:
            #input the form's data into database
            s=defectdata.objects.create(product=cd['product'],layer=cd['layer'],lot=cd['lot'],
            wafer=cd['wafer'],scantime=cd['scantime'],defectcount=cd['defectcount'],remarks=cd['remarks'])
            s.save()
            return HttpResponseRedirect('/database/success/')
    else:
        form=defectdataForm()
    return render(request,'database/registration.html',{'form':form})
    
def success(request):
    return render(request,'database/success.html')  

