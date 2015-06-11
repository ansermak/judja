from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<post_title>[0-9А-ЯЄЇІа-яєїіA-Za-z\s\.\’\,-]+)/$',
        views.post, name='post'),
    url(r'^authors/(?P<post_author>[А-ЯЄЇІа-яєїіA-Za-z\s\-]+)/$',
        views.author, name='author'),
]
