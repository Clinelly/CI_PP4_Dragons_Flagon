from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
        )
    slug = models.SlugField(
        max_length=200, unique=True
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    updated_on = models.DateTimeField(
        auto_now=True
        )
    content = models.TextField()
    approved = models.BooleanField(
        default=False
        )
    likes = models.ManyToManyField(
        User, related_name='likes', blank=True
        )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.content} by {self.author}"

    def number_of_likes(self):
        return self.likes.count()
