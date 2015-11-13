from django.db import models

# Create your models here.
class cpdata(models.Model):
    x=models.DecimalField(max_digits=5, decimal_places=2)
    y=models.DecimalField(max_digits=5, decimal_places=2)
    c=models.CharField(max_length=10)
    f=models.FileField()
