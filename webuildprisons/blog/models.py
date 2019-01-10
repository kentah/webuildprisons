from django.db import models
from webuildprisons.models import TimeStampedModel


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = TimeStampedModel.created
    modified = TimeStampedModel.modified
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)



class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)