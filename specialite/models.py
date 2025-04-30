
# model specialite:
#----------------

from django.db import models
from django.conf import settings

class Specialite(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nom
    
class Cours(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE, related_name='cours')
    formateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cours_donnes')
    stagiaires = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cours_suivis', blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.titre