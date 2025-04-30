# specialite/urls.py
from django.urls import path
from . import views

app_name = 'specialite' # Nom de l'application pour les URL inversées

urlpatterns = [

    # Liste des spécialités (Read - List)
    path('liste/', views.SpecialiteListView.as_view(), name='specialite_list'),

    # Détail d'une spécialité (Read - Detail)
    path('<int:pk>/', views.SpecialiteDetailView.as_view(), name='specialite_detail'),

    # Créer une nouvelle spécialité (Create)
    path('ajouter/', views.SpecialiteCreateView.as_view(), name='specialite_create'),

    # Modifier une spécialité existante (Update)
    path('<int:pk>/modifier/', views.SpecialiteUpdateView.as_view(), name='specialite_update'),

    # Supprimer une spécialité existante (Delete)
    path('<int:pk>/supprimer/', views.SpecialiteDeleteView.as_view(), name='specialite_delete'),
]