from django.urls import path
from .views import (
    StagiaireListView, StagiaireDetailView, StagiaireCreateView,
    StagiaireUpdateView, StagiaireDeleteView
)

app_name = 'stagiaire'

urlpatterns = [
    path('', StagiaireListView.as_view(), name='stagiaire_list'),
    path('<int:pk>/', StagiaireDetailView.as_view(), name='stagiaire_detail'),
    path('ajouter/', StagiaireCreateView.as_view(), name='stagiaire_create'),
    path('<int:pk>/modifier/', StagiaireUpdateView.as_view(), name='stagiaire_update'),
    path('<int:pk>/supprimer/', StagiaireDeleteView.as_view(), name='stagiaire_delete'),
]