from django.db import models

# Create your models here.
class ContactItem(models.Model):
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    email=models.EmailField()