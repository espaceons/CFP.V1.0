from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Formateur
from .forms import FormateurForm
from django.contrib import messages  # Pour les messages flash


class FormateurListView(ListView):
    model = Formateur
    template_name = 'formateur/formateur_list.html'
    context_object_name = 'formateurs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [('Formateurs', '/formateur/')]
        return context

class FormateurDetailView(DetailView):
    model = Formateur
    template_name = 'formateur/formateur_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [('Formateurs', '/formateur/'), (self.object.user.first_name, '')] # A améliorer avec l'URL detail
        return context





#----------
class FormateurCreateView(CreateView):
    model = Formateur
    form_class = FormateurForm
    template_name = 'formateur/formateur_form.html'
    success_url = reverse_lazy('specialite:specialite_list')

    def form_valid(self, form):
        formateur = form.save()
        messages.success(self.request, f"Le formateur '{formateur.nom}' a été créée avec succès.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Veuillez corriger les erreurs dans le formulaire.")
        return super().form_invalid(form)
#----------


class FormateurUpdateView(UpdateView):
    model = Formateur
    form_class = FormateurForm
    template_name = 'formateur/formateur_form.html'
    success_url = reverse_lazy('formateur:formateur_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [('Formateurs', '/formateur/'), ('Modifier', '')]
        return context

class FormateurDeleteView(DeleteView):
    model = Formateur
    template_name = 'formateur/formateur_confirm_delete.html'
    success_url = reverse_lazy('formateur:formateur_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [('Formateurs', '/formateur/'), ('Supprimer', '')]
        return context