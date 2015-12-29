#feeds.py in blog application

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    title='My blog'#correspond to the <title>,<link>,<description> RSS elements respectively
    link='/blog/'
    description='New posts of my blog.'
    
    def items(self):
        '''retrieve the objects to be included in the feed'''
        return Post.objects.filter(status='published')[:5]
        
    def item_title(self,item):
        return item.title
        
    def item_description(self,item):
        return truncatewords(item.body, 30)