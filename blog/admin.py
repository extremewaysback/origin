from django.contrib import admin
from .models import Post, Comment, AboutThisSite

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish','status')
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    #Prepolulate use a bit of javascript to populat from the fields assigned.
    #Automatically generate the value for SlugField fields from one or more other fields. (substituting dashes for spaces)
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','-publish']

admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','created','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Comment, CommentAdmin)
    

class AboutThisSiteAdmin(admin.ModelAdmin):
    list_dispaly=('title', 'slug', 'body')
    prepopulated_fields={'slug':('title',)}
    
admin.site.register(AboutThisSite, AboutThisSiteAdmin)