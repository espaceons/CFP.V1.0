from django.urls import path
from . import views

app_name = 'formateur'

urlpatterns = [
    path('creer/', views.FormateurCreateView.as_view(), name='formateur_create'),  # URL pour créer un formateur
    path('liste/', views.FormateurListView.as_view(), name='formateur_list'),        # URL pour lister les formateurs
    path('detail/<int:pk>/', views.FormateurDetailView.as_view(), name='formateur_detail'),  # Détails d'un formateur
    path('modifier/<int:pk>/', views.FormateurUpdateView.as_view(), name='formateur_update'),  # Mise à jour d'un formateur
    path('supprimer/<int:pk>/', views.FormateurDeleteView.as_view(), name='formateur_delete'),  # Suppression d'un formateur
]