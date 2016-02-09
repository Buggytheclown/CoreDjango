from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .form import PostModel
from posts.models import Post


def posts_list(request):
    model_title = Post.objects.all()
    query = request.GET.get('q')
    if query:
        model_title = Post.objects.all().filter(title__icontains=query)
    paginator = Paginator(model_title, 5)
    page = request.GET.get('page')
    try:
        model_title_p = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        model_title_p = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        model_title_p = paginator.page(paginator.num_pages)
    context = {
        'model_title': model_title_p
    }
    return render(request, 'posts/home.html', context)


def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostModel(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Post successfully created')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)


def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, 'posts/detail.html', context)


def posts_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostModel(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        # some stuff there
        instance.save()
        messages.success(request, 'Post successfully edited')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def posts_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post: %s - was successfully deleted" % (instance.title))
    return redirect('posts:home')
