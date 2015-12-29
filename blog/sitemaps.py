#sitemaps.py file inside blog application

from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq='weekly'
    priority=0.9 #indicate the relevance in website
    
    def items(self):
        '''get all the published posts, get the objects included in this sitemap'''
        return Post.objects.filter(status='published')
        
    def lastmode(self,obj):
        '''returns the last time the object was modified'''
        return obj.publish