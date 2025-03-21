from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# users and their posts in the database
# django has a build in authentication system for user 
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    # auto_now_add update a datetime only when the object is created.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return  reverse('post-detail', kwargs={'pk': self.pk})
