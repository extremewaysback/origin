from django.shortcuts import render


def origin(request):
    return render(request,"origin/newbase.html")
    
    
def reverse_resolution_of_urls(request):
    return render(request,"origin/reverse_resolution_of_urls.html")
    
def test(request):
    return render(request,"origin/html5.html")
    
def w3school(request):
    return render(request,"origin/w3school.html")
    
def newbase(request):
    return render(request,"origin/newbase.html")
    
def newexperience(request):
    return render(request, "origin/newexperience.html")
    
    
def deployment(request):
    return render(request, "origin/deployment.html")
    
def ajax(request):
    return render(request, "origin/ajax.html")
    