# specialite/forms.py
from django import forms
from .models import Specialite

class SpecialiteForm(forms.ModelForm):
    class Meta:
        model = Specialite
        fields = ['nom', 'description'] # Champs du modèle à inclure dans le formulaire
        # Vous pouvez ajouter des labels personnalisés si nécessaire:
        widgets = {  # Pour personnaliser les widgets des champs
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }