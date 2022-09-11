from unicodedata import name
from django.db import models

# Create your models here.
class Host(models.Model):
    name=models.CharField(max_length=30,unique=True)
    address=models.CharField(max_length=70,unique=True)
    port=models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name
        