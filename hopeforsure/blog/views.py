# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from blog.models import Post
 
def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})
 
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
	return render_to_response('blog/index.html', {'posts': s, "likes": s.likes})