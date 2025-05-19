# model formateur:
#----------------
 
from django.db import models
from utilisateur.models import CustomUser
from specialite.models import Specialite

class Formateur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.TextField()
    tel = models.CharField(max_length=12, null=True, blank=True)
    specialites = models.ManyToManyField(Specialite)
    experience = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"