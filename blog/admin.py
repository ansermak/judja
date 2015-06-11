from django.contrib import admin

from .models import Author, Post, Image


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Image)
