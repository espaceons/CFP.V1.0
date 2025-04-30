# specialite/forms.py
from django import forms
from .models import Specialite

class SpecialiteForm(forms.ModelForm):
    class Meta:
        model = Specialite
        fields = ['nom', 'description'] # Champs du modèle à inclure dans le formulaire
        # Vous pouvez ajouter des labels personnalisés si nécessaire:
        # labels = {
        #     'nom': 'Nom de la Spécialité',
        #     'description': 'Description',
        # }
        # Et des widgets pour personnaliser l'apparence (ex: utiliser un Textarea pour la description):
        # widgets = {
        #     'description': forms.Textarea(attrs={'rows': 4}),
        # }