# CpMap urls.py
from django.conf.urls import url
import views

urlpatterns=[
   url(r'^success/$',views.success,name='success'),
   url(r'^cpmap/$',views.upload_file, name='upload_file'),
   url(r'^bar/$',views.barchart, name='barchart'),
   url(r'line/$',views.linechart, name='linechart'),
   ]
