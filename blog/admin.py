from django.contrib import admin
#~ from django_summernote.admin import SummernoteModelAdmin

from .models import Author, Post, Image

class ImageInline(admin.StackedInline):
    model = Image
    extra = 3

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'change_date')

    inlines = [ImageInline]


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Image)
