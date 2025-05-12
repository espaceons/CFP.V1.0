from django.urls import path
from .views import (
    FormateurListView, FormateurDetailView, FormateurCreateView,
    FormateurUpdateView, FormateurDeleteView
)

app_name = 'formateur'

urlpatterns = [
    path('', FormateurListView.as_view(), name='formateur_list'),
    path('<int:pk>/', FormateurDetailView.as_view(), name='formateur_detail'),
    path('ajouter/', FormateurCreateView.as_view(), name='formateur_create'),
    path('<int:pk>/modifier/', FormateurUpdateView.as_view(), name='formateur_update'),
    path('<int:pk>/supprimer/', FormateurDeleteView.as_view(), name='formateur_delete'),
]