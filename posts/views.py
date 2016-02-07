from django.shortcuts import render

# Create your views here.
from posts.models import Post


def posts_list (request):
    model_title = Post.objects.all()
    context = {
        'model_title':model_title
    }
    return render (request, 'posts/home.html', context)

def posts_create (request):
    context = {}
    return render (request, 'posts/create.html', context)

def posts_detail (request):
    context = {}
    return render (request, 'posts/detail.html', context)

def posts_update (request):
    context = {}
    return render (request, 'posts/update.html', context)

def posts_delete (request):
    context = {}
    return render (request, 'posts/delete.html', context)