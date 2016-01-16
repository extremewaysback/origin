#shop/models.py

from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True)#when unique is set, because unique implies the creation of an index
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
        
    def __str__(self):
        return self.name
        
        
class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products')