from statistics import mode
from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    mail = models.EmailField()
    date_naiss = models.DateField()
    phone = models.CharField(max_length=100)


    
