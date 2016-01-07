#account/urls.py
from django.conf.urls import url
from . import views

urlpatterns=[
     #previous login view
     #url(r'^login/$',views.user_login,name='login'), 
     #url(r'logout/$',views.user_logout,name='custom_logout'),  
     #login/logout urls
     url(r'^login/$','django.contrib.auth.views.login',name='login'),#build-in login
     url(r'^logout/$','django.contrib.auth.views.logout',name='logout'),#build-in logout
     url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login'),#buildin logout-then-login
     url(r'^dashboard/$',views.dashboard,name='dashboard'),#dashboard view required login
     url(r'^password-change/$','django.contrib.auth.views.password_change',name='password_change'),#handle the form to change the password 
     url(r'^password-change/done/$','django.contrib.auth.views.password_change_done',name='password_change_done'),#done changing password and display a success message
     url(r'^password-reset/$','django.contrib.auth.views.password_reset',name='password_reset'),
     url(r'^password-reset/done/$','django.contrib.auth.views.password_reset_done',name='password_reset_done'),
     url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$','django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
     url(r'^password-reset/complete/$','django.contrib.auth.views.password_reset_complete',name='password_reset_complete'),
     url(r'^register/$',views.register,name='register'),
     ]