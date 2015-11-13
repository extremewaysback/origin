from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import cpdataForm
from .models import cpdata
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

def cpmap(request):
    if request.method=='POST':
        form=cpdataForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            return render('success')
    else:
        form=cpdataForm()
    return render(request,'CpMap/cpmap.html',{'form':form})

'''   
def register(request):
    if request.method=='POST':
        form=defectdataForm(request.POST) #interface with html
        if form.is_valid():
            cd=form.cleaned_data
            #if cd not in Student.objects:
            #input the form's data into database
            s=defectdata.objects.create(product=cd['product'],layer=cd['layer'],lot=cd['lot'],
            wafer=cd['wafer'],scantime=cd['scantime'],defectcount=cd['defectcount'],remarks=cd['remarks'])
            #s.save()
            return HttpResponseRedirect('/success/')
    else:
        form=defectdataForm()
    return render(request,'database/registration.html',{'form':form})
'''

from django.http import HttpResponse
def barchart(request):

    #instantiate a drawing object
    import mycharts
    d = mycharts.MyBarChartDrawing()

    #extract the request params of interest.
    #I suggest having a default for everything.
    if 'height' in request:
        d.height = int(request['height'])
    if 'width' in request:
        d.width = int(request['width'])
    
    if 'numbers' in request:
        strNumbers = request['numbers']
        numbers = map(int, strNumbers.split(','))    
        d.chart.data = [numbers]   #bar charts take a list-of-lists for data

    if 'title' in request:
        d.title.text = request['title']
  

    #get a GIF (or PNG, JPG, or whatever)
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')
    
    

def linechart(request):

    #instantiate a drawing object
    import mycharts
    d = mycharts.MyLineChartDrawing()

    #extract the request params of interest.
    #I suggest having a default for everything.
    

    d.height = 300
    d.chart.height = 300
    

    d.width = 300
    d.chart.width = 300
   
    d.title._text = request.session.get('Some custom title')
    


    d.XLabel._text = request.session.get('X Axis Labell')
    d.YLabel._text = request.session.get('Y Axis Label')

    d.chart.data = [((1,1), (2,2), (2.5,1), (3,3), (4,5)),((1,2), (2,3), (2.5,2), (3.5,5), (4,6))]
   

    
    labels =  ["Label One","Label Two"]
    if labels:
        # set colors in the legend
        d.Legend.colorNamePairs = []
        for cnt,label in enumerate(labels):
                d.Legend.colorNamePairs.append((d.chart.lines[cnt].strokeColor,label))


    #get a GIF (or PNG, JPG, or whatever)
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')