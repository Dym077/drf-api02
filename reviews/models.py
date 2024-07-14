from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    """
    Review model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=255, blank=True)
    tags = models.CharField(max_length=255, blank=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content