from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Author, Post


def index(request):
    posts = Post.objects.order_by('pub_date').all()
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'posts': posts,
    })
    return HttpResponse(template.render(context))


def post(request, post_title):
    post = Post.objects.get(title=post_title)
    template = loader.get_template('blog/posts/index.html')
    context = RequestContext(request, {
        'post': post,
    })
    return HttpResponse(template.render(context))


def author(request, post_author):
    author = Author.objects.get(name=post_author)
    posts = Post.objects.filter(author=author)
    template = loader.get_template('blog/authors/index.html')
    context = RequestContext(request, {
        'author': author,
        'posts': posts,
    })
    return HttpResponse(template.render(context))
