from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
        #In order to keep code generic,use the get_user_model() method to retrieve the user model and the AUTH_USER_MODEL setting to refer to it
        user=models.OneToOneField(settings.AUTH_USER_MODEL,primary_key=True)
        date_of_birth=models.DateField(blank=True,null=True)
        photo=models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
        
        def __str__(self):
            return 'Profile for user {}'.format(self.user.username)