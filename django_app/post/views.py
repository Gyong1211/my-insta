from django.http import HttpResponse
from django.shortcuts import render
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context=context)


def post_detail(request, post_pk):
    post = Post.objects.get(id=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context=context)

