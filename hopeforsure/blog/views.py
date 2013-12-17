# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from blog.models import Post
 
def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    id = randint(1, 6)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'id': id})
 
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

def top(request):
    # get the blog posts that are published
    top_posts = Post.objects.filter(published=True).order_by('-likes')[:20]
    # now return the rendered template
    return render(request, 'blog/top.html', {'top_posts': top_posts})

def about(request):
    # now return the rendered template
    return render(request, 'blog/about.html')

def upvote(request, slug):
    s = get_object_or_404(Post, slug=slug)
    s.likes += 1
    s.save()
    return HttpResponse(s.likes)

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }

def id(request):
    return HttpResponse(randint(50,100))

def testid(request, slug):
    s = get_object_or_404(Post, slug=slug)
    s.likes += 1
    s.save()
    return HttpResponse(s.likes)

def like(request, slug):
	if request.is_ajax():
		s= get_object_or_404(Post, slug=slug)
		s.likes+=1
		s.save()

		if 'HTTP_REFERER' in request.META:
			return HttpResponseRedirect(request.META['HTTP_REFERER'])
		return HttpResponseRedirect('/')
