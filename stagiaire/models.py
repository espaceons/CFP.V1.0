# stagiaire/models.py

from django.db import models
from utilisateur.models import CustomUser
from specialite.models import Specialite # Assurez-vous que l'application 'specialite' est bien créée et configurée

class Stagiaire(models.Model):
    """
    Modèle représentant un stagiaire dans le centre de formation.
    """
    # Liaison OneToOne avec CustomUser pour gérer l'authentification et les informations de base
    # Assurez-vous que l'utilisateur lié a le rôle 'STAGIAIRE'
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='stagiaire_profile')

    # Informations personnelles du stagiaire
    date_naissance = models.DateField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.TextField()
    specialites = models.ManyToManyField(Specialite)
    # Ajoutez d'autres champs pertinents pour un stagiaire si nécessaire (ex: CIN, niveau d'étude, etc.)

    # Relation avec la spécialité suivie par le stagiaire
    # Un stagiaire peut suivre une ou plusieurs spécialités (Many-to-Many)
    # Ou une seule spécialité (ForeignKey) - adaptez selon votre besoin
    # Ici, j'utilise ManyToManyField, si c'est une seule spécialité, changez pour ForeignKey
    specialites = models.ManyToManyField(Specialite, related_name='stagiaires')

    # Statut du stagiaire (ex: Actif, En pause, Diplômé, Abandon, etc.)
    STATUT_CHOICES = [
        ('ACTIF', 'Actif'),
        ('EN_PAUSE', 'En pause'),
        ('DIPLOME', 'Diplômé'),
        ('ABANDON', 'Abandon'),
        ('INSCRIT', 'Inscrit (en attente de début)'),
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='INSCRIT')

    # Vous pourriez ajouter des champs pour suivre la progression, les paiements, etc.

    def __str__(self):
        """
        Représentation en chaîne de caractères du modèle Stagiaire.
        Utilise le nom et prénom de l'utilisateur lié.
        """
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        """
        Métadonnées pour le modèle Stagiaire.
        """
        verbose_name = "Stagiaire"
        verbose_name_plural = "Stagiaires"
        # Vous pouvez ajouter des contraintes ou des index ici si nécessaire
