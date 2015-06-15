from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    change_date = models.DateTimeField('date_changed', auto_now=True)

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Image(models.Model):
    title = models.CharField(max_length=200)
    post = models.ForeignKey(Post)
    image_file = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
