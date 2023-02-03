from django.db import models
from django.contrib.auth.models import User

# User

class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    price = models.IntegerField()
