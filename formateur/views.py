from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import Formateur
from .forms import FormateurForm

class FormateurCreateView(CreateView):
    model = Formateur
    form_class = FormateurForm
    template_name = 'formateur/formateur_form.html'
    success_url = reverse_lazy('formateur:formateur_list')

    def form_valid(self, form):
        formateur = form.save()
        messages.success(self.request, f"Le formateur '{formateur.user.first_name} {formateur.user.last_name}' a été créé avec succès.")
        return super().form_valid(form)

class FormateurListView(ListView):
    model = Formateur
    template_name = 'formateur/formateur_list.html'
    context_object_name = 'formateurs'
    
    def get_queryset(self):
        # Filtrer les formateurs basés sur le rôle de l'utilisateur
        return Formateur.objects.filter(user__role='FORMATEUR', user__is_active=True) # Récupérer uniquement les formateurs qui sont actifs

class FormateurDetailView(DetailView):
    model = Formateur
    template_name = 'formateur/formateur_detail.html'
    context_object_name = 'formateur'

class FormateurUpdateView(UpdateView):
    model = Formateur
    form_class = FormateurForm
    template_name = 'formateur/formateur_form.html'
    success_url = reverse_lazy('formateur:formateur_list')

    def form_valid(self, form):
        formateur = form.save()
        messages.success(self.request, f"Le formateur '{formateur.user.first_name} {formateur.user.last_name}' a été mis à jour avec succès.")
        return super().form_valid(form)

class FormateurDeleteView(DeleteView):
    model = Formateur
    template_name = 'formateur/formateur_confirm_delete.html'
    success_url = reverse_lazy('formateur:formateur_list')

    def delete(self, request, *args, **kwargs):
        formateur = self.get_object()
        messages.success(self.request, f"Le formateur '{formateur.user.first_name} {formateur.user.last_name}' a été supprimé avec succès.")
        return super().delete(request, *args, **kwargs)