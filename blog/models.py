from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Image(models.Model):
    title = models.CharField(max_length=200)
    file_name = models.CharField(max_length=256)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.title
