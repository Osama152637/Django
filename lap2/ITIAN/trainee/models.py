from django.db import models
from track.models import *

# Create your models here.

class Trainee(models.Model):
    traineeId = models.AutoField(primary_key=True)
    firstName = models.CharField()
    lastName = models.CharField()
    gender = models.CharField(max_length=10, null=True)
    birthData = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11, null=True)
    e-mail = models.EmailField(max_length=100, null=True)
    track = models.ForeignKey("track.Track", on_delete=models.CASCADE)
