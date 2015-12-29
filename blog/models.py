from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Use the reverse() method that allows you to build URLs by their name and passing optional parameters.

#add customised manager 

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES=(
         ('draft','Draft'),
         ('published','Published'),
    )
    
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250, unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts')#many-to-one
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=models.Manager() #The default manager attribute
    #published=PublishedManager() #Our custom manager attribute
    tags=TaggableManager()#Tags manager will allow you to add, retrieve, and remove tags from Post objects.
    
    class Meta:
        ordering=('-publish',)
        
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        '''use the get_absolute_url() in templates, use attributes to get a URL associated with a view'''
        # Through the reverse function, get the related view and passing the args
        return reverse('blog:post_detail',args=[self.publish.year,
                                                self.publish.strftime('%m'),#using the strftime() function to build the URL using month and day with leading zeros.
                                                self.publish.strftime('%d'),
                                                self.slug])

class Comment(models.Model):
    #ForeignKey to associate the comment with a single post. This many-to-one relationship is defined in the Comment model
    #The relate_name attribute allows us to name the attribute that we use for the relation from the related object back to this one.
    #If you don't define teh related_name attribute, django will use the undercase name of the model followed by _set to name the manager of the related object back to this one.
    post=models.ForeignKey(Post, related_name='comments')
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    #active boolen field that we will use to manually deactivate inappropriate comments. 
    active=models.BooleanField(default=True)
    
    class Meta:
        ordering=('created',)
        
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
    