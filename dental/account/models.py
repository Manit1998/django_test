from django.db import models
from django.utils import timezone


class data(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):             
        return self.username