from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    year=models.IntegerField()
    director = models.CharField(max_length=50)