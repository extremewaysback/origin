from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.register),
    url(r'^success/$',views.success),
]