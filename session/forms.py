# session/forms.py

from django import forms
from .models import Session
# Importez les modèles des applications liées pour potentiellement filtrer les choix
from specialite.models import Specialite
from formateur.models import Formateur
from stagiaire.models import Stagiaire

class SessionForm(forms.ModelForm):
    """
    Formulaire basé sur le modèle pour créer ou modifier une session.
    """
    class Meta:
        model = Session
        # Liste des champs à inclure dans le formulaire, maintenant avec les nouveaux champs
        fields = ['nom', 'date_debut', 'date_fin', 'specialites', 'formateurs', 'stagiaires', 'statut', 'lieu', 'capacite_maximale']
        # Définition des widgets pour personnaliser l'apparence des champs HTML
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            # Utilise un input de type date pour les dates
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # Utilise SelectMultiple pour les relations Many-to-Many
            'specialites': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'formateurs': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'stagiaires': forms.SelectMultiple(attrs={'class': 'form-control'}),
            # Ajout des widgets pour les nouveaux champs
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'capacite_maximale': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialise le formulaire.
        Vous pouvez filtrer les querysets des champs ManyToMany ici si nécessaire.
        """
        super(SessionForm, self).__init__(*args, **kwargs)
        # Exemple : filtrer les formateurs actifs si votre modèle Formateur a un champ 'is_active'
        # self.fields['formateurs'].queryset = Formateur.objects.filter(is_active=True)
        # Exemple : filtrer les stagiaires avec un certain statut
        # self.fields['stagiaires'].queryset = Stagiaire.objects.filter(statut='INSCRIT')

    # Vous pouvez ajouter des méthodes de validation personnalisées ici si nécessaire
    def clean(self):
        """
        Validation personnalisée pour vérifier que la date de fin est après la date de début.
        """
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')

        if date_debut and date_fin and date_fin < date_debut:
            raise forms.ValidationError(
                "La date de fin ne peut pas être antérieure à la date de début."
            )
        return cleaned_data
