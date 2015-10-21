#contact/urls.py

from django.conf.urls import url
import views

urlpatterns=[
url(r'^$',views.contact,name='contact'),
url(r'^thanks/$',views.thanks,name='contactthanks')
]