from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"[{self.author.username}]{self.title}"


