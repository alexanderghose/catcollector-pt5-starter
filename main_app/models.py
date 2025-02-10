from django.db import models

# Create your models here.
# this is the django parallel of
# creating mongoose schemas
class Cat(models.Model):
    name = models.CharField(max_length=100) # add a name column
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self): # helps us have better prints of cats
        return self.name
