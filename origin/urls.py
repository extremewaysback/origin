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
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
import views

sitemaps={'posts':PostSitemap}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.origin, name='origin'),  #show the origin homepage of the website
    url(r'^contact/',include('contact.urls')),
    url(r'^subscription/',include('subscription.urls')),
    url(r'^database/',include('database.urls')),
    url(r'^reverse-resolution-of-urls/$',views.reverse_resolution_of_urls, name='reverse_resolution_of_urls'),
    url(r'newbase/$',views.newbase,name='newbase'),
    url(r'deployment/$',views.deployment, name='deployment'),
    url(r'^ajax/$',views.ajax,name='ajax'),
    url(r'^blog/',include('blog.urls',namespace='blog')),#add namespace for reference in template
    url(r'^sitemap\.xml$',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views,sitemap'),
]

#urlpatterns+=[url(r'articles/comments/',include('django_comments.urls'))]