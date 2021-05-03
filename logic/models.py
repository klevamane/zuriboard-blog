from django.db import models

# Create your models here.


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Blog(Timestamp):
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=200)


class Comment(Timestamp):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
