from django.db import models

# Create your models here.

class Clients(modesl.Model):
    
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    