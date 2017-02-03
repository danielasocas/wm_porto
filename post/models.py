from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text