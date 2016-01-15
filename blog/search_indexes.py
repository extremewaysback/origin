#search_indexes.py inside blog applicaiton and register your models here
from haystack import indexes
from .models import Post

#SearchIndex objects are the way haystack determines what data should be placed in the search index and handles the flow of data in

#Every SearchIndex requires there be one (an only one) field with document=True.
#This indicates to both Haystack and the search engine about which field is the primary field for searching within.
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text=indexes.CharField(document=True, use_template=True)
    publish=indexes.DateTimeField(model_attr='publish')#provide additional filtering options.
    
    def get_model(self):
        return Post
        
    def index_queryset(self,using=None):
        '''Only search for the published posts, return a QuerySet'''
        return self.get_model().objects.filter(status='published')
        
#Every SearchIndex requires there be one (and only one) field with document=True. This indicates to both 
#Haystack and search engine about which field is the primary field for searching within  

#When you choose a document=True field, it should be consistently named across all of your SearchIndex classes to avoid confusing the
#backend. The converntion is to name this field text.

#Additionally, we're providing use_template=True on the Text field. This allows us to use a data template (rather than error-prone concatenation) to 
#build the document the search engine will index.

#You will need to create a new template inside your template directory called
#search/indexes/myapp/note_text.txt