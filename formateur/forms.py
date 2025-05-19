from django import forms
from .models import Formateur
from utilisateur.models import CustomUser

class FormateurForm(forms.ModelForm):
    class Meta:
        model = Formateur
        fields = ['nom', 'prenom', 'adresse', 'tel', 'user', 'specialites', 'experience']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),  # Assurez-vous de limiter le queryset ici si nécessaire
            'specialites': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FormateurForm, self).__init__(*args, **kwargs)
        # Limitez le queryset aux utilisateurs ayant le rôle de formateur
        self.fields['user'].queryset = CustomUser.objects.filter(role='FORMATEUR', is_active=True)  # Cela montre uniquement les formateurs