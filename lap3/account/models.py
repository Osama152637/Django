from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=255)
    e-mail = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    trainee = models.ForeignKey("trainee.Trainee", on_delete=models.CASCADE)
