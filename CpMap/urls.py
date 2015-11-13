# cpdata urls.py
from django.conf.urls import url
import views

urlpatterns=[
   url(r'^cpmap/$',views.cpmap, name='cpmap'),
   url(r'^bar/$',views.barchart, name='barchart'),
   url(r'line/$',views.linechart, name='linechart'),
   ]
