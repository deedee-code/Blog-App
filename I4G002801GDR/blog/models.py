from django.db import models

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
