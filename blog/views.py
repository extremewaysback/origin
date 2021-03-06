from django.shortcuts import render, get_object_or_404
from .models import Post, AboutThisSite
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count#This is the Count aggregation function of the Django ORM.
from haystack.query import SearchQuerySet

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
# After you have some knowledge about how to use the ORM, you are ready to build the views of the blog applcaiton
# A Django view is just a Python function that receives a web request and returns a web response
# Inside the view goes all the logic to reutrn the desired response.

def post_share(request, post_id):
    '''handle the forms submitted by users and send an email when it's successfully submitted'''
    post=get_object_or_404(Post, id=post_id, status='published')
    sent=False #A flag passed to template for setting the logic to display different content in template
    
    if request.method=='POST':
        #Form was submitted
        form=EmailPostForm(request.POST) #Initialize an object with request.POST parameters submitted by user
        if form.is_valid():
            #Form fields passed validation
            cd=form.cleaned_data
            #...send email
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{} ({}) recommends you reading "{}"'.format(cd['name'],cd['email'],post.title) #{} replacement fields
            message='read "{}" at {}\n\n{}\'s comments: {}'.format(post.title,post_url, cd['name'], cd['comments'])
            send_mail(subject,message,'extremeways@126.com',[cd['to']])
            sent=True
    else:
        form=EmailPostForm()
        
    return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent})



class PostListView(ListView):
    queryset=Post.objects.filter(status='published')
    context_object_name='posts'
    paginate_by=3
    template_name='blog/post/list.html'

# This is analogous to the previous post_list view.


def post_list(request,tag_slug=None):
    '''render the posts published'''
    
    object_list=Post.objects.filter(status='published')
    
    #Get a list of tags which are attached to Post class
    set_list=[set(o.tags.all()) for o in object_list]
    tags=set()
    for s in set_list:
        tags=tags|s  #union of set
    tags=[t.name for t in list(tags)]
    tag_list_all=', '.join(tags)
    
    #If there is a tag_slug through URL, will present the posts containing the given tag.
    #Show the posts paginated
    #tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)#Get the tag specified by tag_slug
        tag_list_all=tag.name
        object_list=object_list.filter(tags__in=[tag])#many to many relationship
    paginator=Paginator(object_list,5) #5 posts in each page
    page=request.GET.get('page')  #get the current page
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliever the first page
        posts=paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts=paginator.page(paginator.num_pages)
        
        
    return render(request,'blog/post/list.html',{'page':page,'posts':posts,'tags':tag_list_all})
    
def post_detail(request, year, month, day, post):
    '''dispaly a single post'''
    #Get the post object through the passed parameters
    try:
        post=Post.objects.get(slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    except:
        post=Post.objects.get(slug=post,status='published')
    
    #Get the comments QuerySet through post object (foreign key of Comment class)
    comments=post.comments.filter(active=True)#post is an object of Post
    if request.method=='POST':#add post in admin site
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():#If the form is invalid, we render the template with the validation errors.
            new_comment=comment_form.save(commit=False)#save() method creates an instance of the model that is linked to and saves it to the database.
            new_comment.post=post#update the post attribute of comment
            #save the comment to the database
            new_comment.save()
    else:
        comment_form=CommentForm()
                            
    #List of similar posts
    #values_list() QuerySet returns tuples with the values for the given fields.
    #Passing it flat=True to get a flat list like [1,2,3,...]
    post_tags_ids=post.tags.values_list('id',flat=True)
    similar_posts=Post.objects.filter(tags__in=post_tags_ids,status='published').exclude(id=post.id)#exclude current post
    
    #Use Count aggregation function to generate a calculated field same_tags that contains the nuber of tags shared with all the tags queried.
    similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    return render(request,'blog/post/detail.html',{'post':post,'comments':comments,'comment_form':comment_form})
    
def post_search(request):
    form=SearchForm()
    cd=None
    results=SearchQuerySet().none()
    total_results=None
    if 'query' in request.GET:#submit the form using the GET method so that the resulting URL includes the query parameter
        form=SearchForm(request.GET)
        if form.is_valid():
            cd=form.cleaned_data
            r=SearchQuerySet().models(Post).filter(content=cd['query'])#return a SearchQuerySet
            #pk_list=[i.pk for i in r]
            results=Post.objects.filter(pk__in=r.values_list('pk',flat=True)) #assign a list of objects to the reuslts
            #count total results
            total_results=r.count()
            
    return render(request,'blog/post/search.html',{'form':form,'cd':cd,'results':results,'total_results':total_results})


def about_site(request, slug=None):
    '''Introduction about this site'''
    aso=get_object_or_404(AboutThisSite, slug=slug)
    return render(request,'blog/post/about-site.html',{'aso':aso})
    