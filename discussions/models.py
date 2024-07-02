from django.db import models
from users.models import User  # Assuming User model is defined in users app
 # Assuming Hashtag model is defined in same app


from django.db import models

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Discussion(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='discussions')
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    likes = models.ManyToManyField(User, related_name='liked_discussions')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:50]


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_comments')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]