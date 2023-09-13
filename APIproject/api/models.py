from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, default='Title')
    description = models.TextField(default='Description...')

    def __str__(self):
        return self.title