from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.PositiveIntegerField()
    balance = models.FloatField(default=0.0)