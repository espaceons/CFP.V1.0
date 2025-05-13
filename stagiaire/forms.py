from django import forms

from utilisateur.models import CustomUser
from .models import Stagiaire
from specialite.models import Specialite

class StagiaireForm(forms.ModelForm):
    class Meta:
        model = Stagiaire
        fields = ['nom', 'prenom', 'adresse', 'tel', 'user', 'specialite']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'specialite': forms.Select(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        formateurs = CustomUser.objects.filter(role='FORMATEUR')
        if formateurs.exists():
            self.fields['user'].queryset = formateurs
        else:
            self.fields['user'].widget = forms.HiddenInput() # Cache le champ
            self.fields['user'].help_text = "Aucun formateur disponible."
            