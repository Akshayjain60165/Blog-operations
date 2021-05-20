from django.db import models

# Create your models here.

class blog(models.Model):
    blog_id = models.IntegerField(primary_key = True)
    place  = models.CharField(max_length = 255)
    title = models.TextField()

class blog_comments(models.Model):
    blog_id = models.IntegerField(primary_key = False)
    comm = models.TextField()

