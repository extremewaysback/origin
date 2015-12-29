from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
    
class Choice(models.Model):
    # many to one
    question=models.ForeignKey(Question)#reference key which matches to the primary key of Question
    choice_text=models.CharField(max_length=200) 
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
       
    