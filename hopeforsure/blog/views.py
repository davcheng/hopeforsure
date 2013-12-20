# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Post
from math import ceil

# calculate total number of pages available
post_count=Post.objects.count()
total_pages = ceil(post_count/3) 

def index(request):
    # set the current page
    current_page = 1
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)[:3]
    # get the posts for the widget but exclude currently displayed posts
    slugs_to_exclude = [post.slug for post in posts] 
    widget_posts = Post.objects.filter(published=True).exclude(slug__in=slugs_to_exclude).order_by('?')[:5]
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'widget_posts': widget_posts, 'current_page': current_page, 'total_pages': total_pages})

def nextfiveposts(request, current_page):
    # get the blog posts that are published
    current_page=int(current_page)
    # get total number of posts
    post_count=Post.objects.count()
    # next page available?
    if current_page<=ceil(post_count/3):
        current_page+=1
    # get and filter posts
    posts = Post.objects.filter(published=True)[3*(current_page-1):3*(current_page)]
   # get the posts for the widget but exclude currently displayed posts
    slugs_to_exclude = [post.slug for post in posts] 
    widget_posts = Post.objects.filter(published=True).exclude(slug__in=slugs_to_exclude).order_by('?')[:5]
 
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'current_page': current_page, 'widget_posts': widget_posts, 'total_pages': total_pages})

def backfiveposts(request, current_page):
    # get the index of the current posts that are on the page
    current_page=int(current_page)
    # back pages available?
    if current_page>1:
        current_page-=1
    # get and filter posts
    posts = Post.objects.filter(published=True)[3*(current_page-1):3*(current_page)]
   # get the posts for the widget but exclude currently displayed posts
    slugs_to_exclude = [post.slug for post in posts] 
    widget_posts = Post.objects.filter(published=True).exclude(slug__in=slugs_to_exclude).order_by('?')[:5]
 
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'current_page': current_page, 'widget_posts': widget_posts,'total_pages': total_pages})

def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # get the posts for the widget, exclude current post
    widget_posts = Post.objects.filter(published=True).exclude(slug=slug).order_by('?')[:5]
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post, 'widget_posts': widget_posts})

def top(request):
    # get the blog posts that are published
    top_posts = Post.objects.filter(published=True).order_by('-likes')[:5]
    # get the posts for the widget but exclude currently displayed posts
    slugs_to_exclude = [post.slug for post in top_posts] 
    widget_posts = Post.objects.filter(published=True).exclude(slug__in=slugs_to_exclude).order_by('?')[:5]
    # now return the rendered template
    return render(request, 'blog/top.html', {'top_posts': top_posts, 'widget_posts': widget_posts})

def random(request):
    # get the Post object
    rand_posts = Post.objects.filter(published=True).order_by('?')[:1]
    # get the posts for the widget but exclude currently displayed posts
    slugs_to_exclude = [post.slug for post in rand_posts] 
    widget_posts = Post.objects.filter(published=True).exclude(slug__in=slugs_to_exclude).order_by('?')[:5]
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post, 'widget_posts': widget_posts})

# multiple random posts
# def random(request):
#     current_page = 1
#     # get the blog posts that are published
#     rand_posts = Post.objects.filter(published=True).order_by('?')[:3]
#     # get the posts for the widget but exclude currently displayed posts
#     slugs_to_exclude = [post.slug for post in rand_posts] 
#     widget_posts = Post.objects.filter(published=True).exclude(slug__in=slugs_to_exclude).order_by('?')[:5]
#     # now return the rendered template
#     return render(request, 'blog/random.html', {'posts': rand_posts, 'widget_posts': widget_posts, 'current_page': current_page})

def about(request):
    # now return the rendered template
    return render(request, 'blog/about.html')

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }

def like(request, slug):
	if request.is_ajax():
        # get current post and increment like count
		s= get_object_or_404(Post, slug=slug)
		s.likes+=1
		s.save()

		if 'HTTP_REFERER' in request.META:
			return HttpResponseRedirect(request.META['HTTP_REFERER'])
		return HttpResponseRedirect('/')
