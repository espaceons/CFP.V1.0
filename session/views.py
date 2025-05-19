# session/views.py

from django.urls import reverse_lazy # Utilisé pour rediriger après succès
from django.views.generic import (
    CreateView, # Vue pour créer un objet
    ListView,   # Vue pour afficher une liste d'objets
    UpdateView, # Vue pour modifier un objet existant
    DeleteView, # Vue pour supprimer un objet existant
    DetailView  # Vue pour afficher les détails d'un objet
)
from django.contrib import messages # Pour afficher des messages de succès ou d'erreur
from .models import Session # Importe le modèle Session
from .forms import SessionForm # Importe le formulaire SessionForm

# Optionnel : Importer les mixins de connexion requise si vous voulez restreindre l'accès
# from django.contrib.auth.mixins import LoginRequiredMixin

class SessionCreateView(CreateView):
    """
    Vue pour créer une nouvelle session.
    """
    model = Session # Le modèle à utiliser
    form_class = SessionForm # Le formulaire à utiliser
    template_name = 'session/session_form.html' # Le template à rendre
    # URL vers laquelle rediriger après la création réussie
    success_url = reverse_lazy('session:session_list')
    # Optionnel : login_required = True # Si vous utilisez LoginRequiredMixin

    def form_valid(self, form):
        """
        Cette méthode est appelée lorsque le formulaire est valide.
        Ajoute un message de succès avant la redirection.
        """
        # Sauvegarde le formulaire pour créer l'objet Session
        session = form.save()
        # Ajoute un message de succès qui sera affiché à l'utilisateur
        messages.success(self.request, f"La session '{session.nom}' a été créée avec succès.")
        # Appelle la méthode parente pour continuer le processus (redirection)
        return super().form_valid(form)

class SessionListView(ListView):
    """
    Vue pour afficher la liste de toutes les sessions.
    """
    model = Session # Le modèle à lister
    template_name = 'session/session_list.html' # Le template à rendre
    context_object_name = 'sessions' # Nom de la variable de contexte dans le template
    # Optionnel : login_required = True # Si vous utilisez LoginRequiredMixin

    def get_queryset(self):
        """
        Retourne le queryset des sessions à afficher.
        Vous pouvez filtrer ou trier ici si nécessaire.
        """
        # Récupérer toutes les sessions, triées par date de début par défaut (défini dans Meta du modèle)
        return Session.objects.all()
        # Exemple : filtrer les sessions futures
        # from django.utils import timezone
        # return Session.objects.filter(date_fin__gte=timezone.now().date())

class SessionDetailView(DetailView):
    """
    Vue pour afficher les détails d'une session spécifique.
    """
    model = Session # Le modèle à utiliser
    template_name = 'session/session_detail.html' # Le template à rendre
    context_object_name = 'session' # Nom de la variable de contexte dans le template
    # Optionnel : login_required = True # Si vous utilisez LoginRequiredMixin

    def get_queryset(self):
        """
        Optimisation : pré-charger les relations ManyToMany pour éviter les requêtes N+1.
        """
        return super().get_queryset().prefetch_related('specialites', 'formateurs', 'stagiaires')

class SessionUpdateView(UpdateView):
    """
    Vue pour modifier une session existante.
    """
    model = Session # Le modèle à utiliser
    form_class = SessionForm # Le formulaire à utiliser
    template_name = 'session/session_form.html' # Le template à rendre (souvent le même que pour la création)
    # URL vers laquelle rediriger après la modification réussie
    success_url = reverse_lazy('session:session_list')
    # Optionnel : login_required = True # Si vous utilisez LoginRequiredMixin

    def form_valid(self, form):
        """
        Cette méthode est appelée lorsque le formulaire est valide.
        Ajoute un message de succès avant la redirection.
        """
        # Sauvegarde le formulaire pour mettre à jour l'objet Session
        session = form.save()
        # Ajoute un message de succès
        messages.success(self.request, f"La session '{session.nom}' a été mise à jour avec succès.")
        # Appelle la méthode parente pour continuer le processus
        return super().form_valid(form)

class SessionDeleteView(DeleteView):
    """
    Vue pour supprimer une session existante.
    """
    model = Session # Le modèle à utiliser
    template_name = 'session/session_confirm_delete.html' # Template de confirmation de suppression
    # URL vers laquelle rediriger après la suppression réussie
    success_url = reverse_lazy('session:session_list')
    # Optionnel : login_required = True # Si vous utilisez LoginRequiredMixin

    def delete(self, request, *args, **kwargs):
        """
        Cette méthode est appelée lors de la suppression de l'objet.
        Ajoute un message de succès avant la redirection.
        """
        # Récupère l'objet à supprimer
        session = self.get_object()
        # Ajoute un message de succès
        messages.success(self.request, f"La session '{session.nom}' a été supprimée avec succès.")
        # Appelle la méthode parente pour effectuer la suppression et la redirection
        return super().delete(request, *args, **kwargs)
