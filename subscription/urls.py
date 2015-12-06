#subscription urls.py

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.subscription,name='subscription'),
    url(r'^success/$',views.success),
]