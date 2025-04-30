# specialite/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,    DetailView,    CreateView,    UpdateView,    DeleteView
from .models import Specialite
from .forms import SpecialiteForm # Importer le formulaire



    
    
# Vue pour lister toutes les spécialités
class SpecialiteListView(ListView):
    model = Specialite
    template_name = 'specialite/specialite_list.html' # Chemin vers le template
    context_object_name = 'specialites' # Nom de la variable dans le template

# Vue pour afficher les détails d'une spécialité
class SpecialiteDetailView(DetailView):
    model = Specialite
    template_name = 'specialite/specialite_detail.html' # Chemin vers le template
    context_object_name = 'specialite' # Nom de la variable dans le template

# Vue pour créer une nouvelle spécialité
class SpecialiteCreateView(CreateView):
    model = Specialite
    form_class = SpecialiteForm # Utiliser le formulaire défini
    template_name = 'specialite/specialite_form.html' # Template pour le formulaire
    success_url = reverse_lazy('specialite:specialite_list') # Redirection après succès

# Vue pour modifier une spécialité existante
class SpecialiteUpdateView(UpdateView):
    model = Specialite
    form_class = SpecialiteForm # Utiliser le formulaire défini
    template_name = 'specialite/specialite_form.html' # Template pour le formulaire
    context_object_name = 'specialite' # Nom de la variable dans le template
    success_url = reverse_lazy('specialite:specialite_list') # Redirection après succès

# Vue pour supprimer une spécialité
class SpecialiteDeleteView(DeleteView):
    model = Specialite
    template_name = 'specialite/specialite_confirm_delete.html' # Template de confirmation
    context_object_name = 'specialite' # Nom de la variable dans le template
    success_url = reverse_lazy('specialite:specialite_list') # Redirection après succès