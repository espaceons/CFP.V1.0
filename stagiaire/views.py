from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Stagiaire
from .forms import StagiaireForm


class StagiaireListView(ListView):
    model = Stagiaire
    template_name = 'stagiaire/stagiaire_list.html'
    context_object_name = 'stagiaires'

class StagiaireDetailView(DetailView):
    model = Stagiaire
    template_name = 'stagiaire/stagiaire_detail.html'

class StagiaireCreateView(CreateView):
    model = Stagiaire
    form_class = StagiaireForm
    template_name = 'stagiaire/stagiaire_form.html'
    success_url = reverse_lazy('stagiaire:stagiaire_list') #Utiliser reverse_lazy pour les vues génériques

class StagiaireUpdateView(UpdateView):
    model = Stagiaire
    form_class = StagiaireForm
    template_name = 'stagiaire/stagiaire_form.html'
    success_url = reverse_lazy('stagiaire:stagiaire_list')

class StagiaireDeleteView(DeleteView):
    model = Stagiaire
    template_name = 'stagiaire/stagiaire_confirm_delete.html'
    success_url = reverse_lazy('stagiaire:stagiaire_list')