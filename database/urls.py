from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.register,name='database'),
    url(r'^success/$',views.success,name='databasesuccess'),
]