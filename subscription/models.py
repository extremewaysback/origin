from django.db import models

# Create your models here.
class Subscribers(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=10)
    
    def __str__(self):
        return self.email
    