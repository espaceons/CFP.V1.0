
# model utilisateur:
#----------------


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrateur'),
        ('FORMATEUR', 'Formateur'),
        ('STAGIAIRE', 'Stagiaire'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='STAGIAIRE')
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username