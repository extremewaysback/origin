from django.db import models
from django.utils.timezone import now

# Create your models here.

LAYER_CHOICES=[
      ('ACT_ADI','ACT_ADI'),
      ('ACT_AEI','ACT_AEI'),
      ('PLY1_ADI','PLY1_ADI'),
      ('PLY1_AEI','PLY1_AEI'),
      ('MET1_ADI','MET1_ADI'),
      ('MET1_AEI','MET1_AEI'),
      ]

class defectdata(models.Model):
    product=models.CharField(max_length=30)
    layer=models.CharField(max_length=30,choices=LAYER_CHOICES)
    lot=models.CharField(max_length=10)
    wafer=models.CharField(max_length=10)
    scantime=models.DateTimeField(default=now)
    defectcount=models.IntegerField()
    remarks=models.TextField()
    
    def __str__(self):
        return self.product+"_"+self.layer+"_"+self.lot+"_"+self.wafer+str(self.defectcount)