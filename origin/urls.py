"""origin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.origin, name='origin'),  #show the origin homepage of the website
    url(r'^contact/',include('contact.urls')),
    url(r'^subscription/',include('subscription.urls')),
    url(r'^database/',include('database.urls')),
    url(r'^reverse-resolution-of-urls/$',views.reverse_resolution_of_urls, name='reverse_resolution_of_urls'),
    url(r'test/$',views.test, name='test'),
    url(r'w3school/$',views.w3school,name='w3school'),
    url(r'newbase/$',views.newbase,name='newbase'),
    #url(r'newexperience/$',views.newexperience,name='newexperience'),
    #url(r'^charts/',include('CpMap.urls'),name='cpmap'),
    #url(r'^articles/comments/',include('django_comments.urls')),
    
]
