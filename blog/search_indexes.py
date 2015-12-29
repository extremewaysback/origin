#search_indexes.py inside blog applicaiton and register your models here
from haystack import indexes
from .models import Post



#Every SearchIndex requires there be one (an only one) field with document=True.
#This indicates to both Haystack and the search engine about which field is the primary field for searching within.
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text=indexes.CharField(document=True, use_template=True)
    publish=indexes.DateTimeField(model_attr='publish')
    
    def get_model(self):
        return Post
        
    def index_queryset(self,using=None):
        return self.get_model().objects.filter(status='published')
        
  