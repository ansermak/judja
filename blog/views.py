from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
# from django.views import generic

from .forms import AuthorForm
from .models import Author, Post, Image


# class IndexView(generic.ListView):
#     template_name = 'blog/index.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         return Post.objects.order_by('-pub_date').all()


def index(request):
    posts = Post.objects.order_by('-pub_date').all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post(request, post_title):
    post = get_object_or_404(Post, title=post_title)
    images = Image.objects.filter(post=post).all()
    context = {'post': post, 'images':images}
    return render(request, 'blog/post.html', context)


def author(request, post_author):
    author = get_object_or_404(Author, name=post_author)
    posts = Post.objects.filter(author=author)
    context = {'author': author,
               'posts': posts,
               }
    return render(request, 'blog/author.html', context)


def new_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = AuthorForm()
    return render(request, 'blog/new_author.html', {'form': form})
