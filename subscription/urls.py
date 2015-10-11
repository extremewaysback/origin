#subscription urls.py

from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$',views.subscription),
    url(r'^success/$',views.success),
]