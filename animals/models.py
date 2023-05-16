from django.db import models

# Create your models here.
class Animal(models.Model):
    type = models.CharField(max_length=128)
    