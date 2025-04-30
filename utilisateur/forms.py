from django import forms
from django.contrib.auth import get_user_model


from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


User = get_user_model()

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'phone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Exclure le rôle 'ADMIN' des choix
            self.fields['role'].choices = [
                (key, label) for key, label in CustomUser.ROLE_CHOICES if key != 'ADMIN'
            ]




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'phone', 'password1', 'password2')