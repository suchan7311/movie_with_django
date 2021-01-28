from django.db import models

# Create your models here.

class Review(models.Model):
    movieTitle=models.CharField(max_length=255,default='')
    name=models.CharField(max_length=255)
    reviewText=models.TextField()
    reviewScore=models.IntegerField(default=0)