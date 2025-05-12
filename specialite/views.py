# specialite/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,    DetailView,    CreateView,    UpdateView,    DeleteView
from .models import Specialite
from .forms import SpecialiteForm # Importer le formulaire
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages  # Pour les messages flash



    
    
# Vue pour lister toutes les spécialités

def specialite_list(request):
    specialites = Specialite.objects.all()
    paginator = Paginator(specialites, 10) # 10 spécialités par page
    page = request.GET.get('page')
    try:
        specialites = paginator.page(page)
    except PageNotAnInteger:
        specialites = paginator.page(1)
    except EmptyPage:
        specialites = paginator.page(paginator.num_pages)
    return render(request, 'specialite/specialite_list.html', {'specialites': specialites})


# Vue pour afficher les détails d'une spécialité

class SpecialiteDetailView(DetailView):
    model = Specialite
    template_name = 'specialite/specialite_detail.html' # Chemin vers le template
    context_object_name = 'specialite' # Nom de la variable dans le template


# Vue pour cree une spécialité

class SpecialiteCreateView(CreateView):
    model = Specialite
    form_class = SpecialiteForm
    template_name = 'specialite/specialite_form.html'
    success_url = reverse_lazy('specialite:specialite_list')

    def form_valid(self, form):
        specialite = form.save()
        messages.success(self.request, f"La spécialité '{specialite.nom}' a été créée avec succès.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Veuillez corriger les erreurs dans le formulaire.")
        return super().form_invalid(form)

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