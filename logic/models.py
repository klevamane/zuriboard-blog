from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(Timestamp):
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=250)


class Comment(Timestamp):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=250)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
