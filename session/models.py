# session/models.py

from django.db import models
# Importez les modèles des applications liées
from specialite.models import Specialite
from formateur.models import Formateur
from stagiaire.models import Stagiaire
from django.core.exceptions import ValidationError


class Session(models.Model):
    """
    Modèle représentant une session de formation.
    Une session regroupe des stagiaires, des formateurs et couvre certaines spécialités
    sur une période donnée.
    """
    nom = models.CharField(max_length=255, help_text="Nom ou titre de la session (ex: Session Printemps 2025)")
    date_debut = models.DateField(help_text="Date de début de la session")
    date_fin = models.DateField(help_text="Date de fin de la session")

    # Relations Many-to-Many avec les autres modèles
    # Une session peut couvrir plusieurs spécialités
    specialites = models.ManyToManyField( Specialite, related_name='sessions', help_text="Spécialités couvertes par cette session" )

    # Une session peut être enseignée par plusieurs formateurs
    formateurs = models.ManyToManyField( Formateur, related_name='sessions', help_text="Formateurs assignés à cette session" )

    # Une session contient plusieurs stagiaires
    stagiaires = models.ManyToManyField( Stagiaire, related_name='sessions', help_text="Stagiaires inscrits à cette session" )

    # Nouveaux champs ajoutés
    STATUT_CHOICES = [
        ('OUVERTE', 'Ouverte'),
        ('EN_COURS', 'En cours'),
        ('TERMINEE', 'Terminée'),
        ('FERMEE', 'Fermée'), # Pourrait signifier complète ou annulée
    ]
    statut = models.CharField( max_length=20, choices=STATUT_CHOICES, default='OUVERTE', help_text="Statut actuel de la session" )
    lieu = models.CharField( max_length=255, null=True, blank=True, help_text="Lieu où se déroule la session" )
    capacite_maximale = models.IntegerField( null=True, blank=True, help_text="Nombre maximal de stagiaires pour cette session" )

    def __str__(self):
        """
        Représentation en chaîne de caractères du modèle Session.
        """
        # Formatage pour afficher le nom et les dates de la session
        return f"{self.nom} ({self.date_debut.strftime('%Y-%m-%d')} - {self.date_fin.strftime('%Y-%m-%d')})"

    class Meta:
        """
        Métadonnées pour le modèle Session.
        """
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
        # Contrainte pour s'assurer que la date de fin n'est pas antérieure à la date de début
        constraints = [
            models.CheckConstraint(
                check=models.Q(date_fin__gte=models.F('date_debut')),
                name='date_fin_gte_date_debut'
            )
        ]
        # Tri par défaut (par date de début, par exemple)
        ordering = ['date_debut', 'nom']

    def clean(self):
        # Vérifiez si le stagiaire est déjà inscrit dans une session de la même spécialité
        for stagiaire in self.stagiaires.all():
            for specialite in self.specialites.all():
                if stagiaire.sessions.filter(specialites=specialite).exists():
                    raise ValidationError(f"{stagiaire} est déjà inscrit à une session de la spécialité {specialite}.")