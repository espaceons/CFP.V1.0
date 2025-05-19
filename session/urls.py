# session/urls.py

from django.urls import path
from . import views # Importe les vues de l'application session

# Définit le nom de l'application pour l'utiliser dans les URLs nommées (ex: 'session:session_list')
app_name = 'session'

urlpatterns = [
    # URL pour créer une nouvelle session
    path('creer/', views.SessionCreateView.as_view(), name='session_create'),

    # URL pour afficher la liste de toutes les sessions
    path('liste/', views.SessionListView.as_view(), name='session_list'),

    # URL pour afficher les détails d'une session spécifique (identifiée par sa clé primaire 'pk')
    path('detail/<int:pk>/', views.SessionDetailView.as_view(), name='session_detail'),

    # URL pour modifier les informations d'une session spécifique
    path('modifier/<int:pk>/', views.SessionUpdateView.as_view(), name='session_update'),

    # URL pour supprimer une session spécifique
    path('supprimer/<int:pk>/', views.SessionDeleteView.as_view(), name='session_delete'),

    # Ajoutez d'autres URLs si vous avez d'autres fonctionnalités spécifiques aux sessions
]
