
# model stagiaire:
#----------------


from django.db import models
from utilisateur.models import CustomUser
from specialite.models import Specialite

class Stagiaire(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite, on_delete=models.SET_NULL, null=True)
    date_inscription = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"