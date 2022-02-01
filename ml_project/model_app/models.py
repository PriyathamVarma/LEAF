from django.db import models
from enum import unique
# Create your models here.


class Leaf(models.Model):

    sepal_length = models.IntegerField()
    sepal_width  = models.IntegerField()  
    petal_length = models.IntegerField()
    petal_width  = models.IntegerField()   