from django.db import models

class Tweet(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='tweet_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)