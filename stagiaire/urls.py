# stagiaire/urls.py

from django.urls import path
from . import views # Importe les vues de l'application stagiaire

# Définit le nom de l'application pour l'utiliser dans les URLs nommées (ex: 'stagiaire:stagiaire_list')
app_name = 'stagiaire'

urlpatterns = [
    # URL pour créer un nouveau stagiaire
    path('creer/', views.StagiaireCreateView.as_view(), name='stagiaire_create'),

    # URL pour afficher la liste de tous les stagiaires
    path('liste/', views.StagiaireListView.as_view(), name='stagiaire_list'),

    # URL pour afficher les détails d'un stagiaire spécifique (identifié par sa clé primaire 'pk')
    path('detail/<int:pk>/', views.StagiaireDetailView.as_view(), name='stagiaire_detail'),

    # URL pour modifier les informations d'un stagiaire spécifique
    path('modifier/<int:pk>/', views.StagiaireUpdateView.as_view(), name='stagiaire_update'),

    # URL pour supprimer un stagiaire spécifique
    path('supprimer/<int:pk>/', views.StagiaireDeleteView.as_view(), name='stagiaire_delete'),

    # Ajoutez d'autres URLs si vous avez d'autres fonctionnalités spécifiques aux stagiaires
]
