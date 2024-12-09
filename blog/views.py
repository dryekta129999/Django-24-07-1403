from xml.etree.ElementInclude import include

from django.shortcuts import render

# Create your views here.

def show_post(request):
	return render(request, 'blog/show_post.html')



def detail_post(request):
	return render(request, 'blog/detail.html')


def new_post(request):
	return render(request, 'blog/new_post.html')