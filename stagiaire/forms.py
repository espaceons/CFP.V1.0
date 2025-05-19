# stagiaire/forms.py

from django import forms
from .models import Stagiaire
from utilisateur.models import CustomUser # Assurez-vous d'importer votre modèle CustomUser

class StagiaireForm(forms.ModelForm):
    """
    Formulaire basé sur le modèle pour créer ou modifier un stagiaire.
    """
    class Meta:
        model = Stagiaire
        # Liste des champs à inclure dans le formulaire
        fields = ['user','nom', 'prenom', 'adresse', 'date_naissance', 'specialites', 'statut']
        # Définition des widgets pour personnaliser l'apparence des champs HTML
        widgets = {
            # Le champ 'user' sera un Select, limité aux utilisateurs ayant le rôle STAGIAIRE
            'user': forms.Select(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # Utilise un input de type date
            'specialites': forms.SelectMultiple(attrs={'class': 'form-control'}), # Permet de sélectionner plusieurs spécialités
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialise le formulaire.
        Limite le queryset du champ 'user' aux utilisateurs qui sont des stagiaires actifs.
        """
        super(StagiaireForm, self).__init__(*args, **kwargs)
        # Limitez le queryset aux utilisateurs ayant le rôle de stagiaire et qui sont actifs
        # Assurez-vous que le rôle 'STAGIAIRE' correspond bien à celui défini dans votre modèle CustomUser
        self.fields['user'].queryset = CustomUser.objects.filter(role='STAGIAIRE', is_active=True)
        # Vous pouvez également ajouter un label plus explicite
        self.fields['user'].label = "Utilisateur (lié au compte stagiaire)"

    # Vous pouvez ajouter des méthodes de validation personnalisées ici si nécessaire
    # def clean_tel(self):
    #     tel = self.cleaned_data.get('tel')
    #     # Ajoutez votre logique de validation pour le numéro de téléphone ici
    #     return tel
