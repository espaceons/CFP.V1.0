# model formateur:
#----------------
 
from django.db import models
from utilisateur.models import CustomUser
from specialite.models import Specialite

class Formateur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialites = models.ManyToManyField(Specialite)
    experience = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"