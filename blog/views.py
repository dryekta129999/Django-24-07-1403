from xml.etree.ElementInclude import include
from .models import Post
from django.shortcuts import render

# Create your views here.

def show_post(request):
	posts = Post.objects.all()
	return render(request, 'blog/show_post.html', {'posts': posts})



def detail_post(request,id):
	post = Post.objects.get(id=id)
	return render(request, 'blog/detail.html', {'post': post})


def new_post(request):
	return render(request, 'blog/new_post.html')