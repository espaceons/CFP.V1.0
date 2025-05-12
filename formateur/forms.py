from django import forms
from .models import Formateur
from specialite.models import Specialite  # Importer le modèle Specialite

class FormateurForm(forms.ModelForm):
    class Meta:
        model = Formateur
        fields = ['user', 'specialites', 'experience']
        widgets = {
            'specialites': forms.CheckboxSelectMultiple(), # Permet de selectionner plusieurs specialités
        }