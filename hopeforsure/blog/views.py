# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Post
 
def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)[:3]
    # posts ordered by number of likes today
    widget_posts = Post.objects.filter(published=True).order_by('-likes')[5:]
    current_page = 1
    # todays_likes = Post.objects.order_by(-likes, date=date.today())
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'widget_posts': widget_posts, 'current_page': current_page})

def nextfiveposts(request, current_page):
    # get the blog posts that are published
    current_page=int(current_page)
    #make this a variable
    posts = Post.objects.filter(published=True)[3*current_page:5*current_page]
    # posts ordered by number of likes today
    current_page+=1
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'current_page': current_page})
 
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

def top(request):
    # get the blog posts that are published
    top_posts = Post.objects.filter(published=True).order_by('-likes')[:10]
    # now return the rendered template
    return render(request, 'blog/top.html', {'top_posts': top_posts})

def about(request):
    # now return the rendered template
    return render(request, 'blog/about.html')

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }

def like(request, slug):
	if request.is_ajax():
		s= get_object_or_404(Post, slug=slug)
		s.likes+=1
		s.save()

		if 'HTTP_REFERER' in request.META:
			return HttpResponseRedirect(request.META['HTTP_REFERER'])
		return HttpResponseRedirect('/')
