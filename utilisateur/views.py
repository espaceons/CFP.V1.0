from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserForm
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth import login



User = get_user_model()


@user_passes_test(lambda u: u.role == 'ADMIN')  # Vérifiez si l'utilisateur est administrateur
def toggle_user_active(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()
    return redirect('utilisateur:utilisateur_list')

@login_required
def utilisateur_list(request):
    utilisateurs = User.objects.all()
    return render(request, 'utilisateur/utilisateur_list.html', {'utilisateurs': utilisateurs})

@login_required
def utilisateur_create(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utilisateur:utilisateur_list')
    else:
        form = CustomUserForm()
    return render(request, 'utilisateur/utilisateur_form.html', {'form': form})

@login_required
def utilisateur_update(request, pk):
    utilisateur = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('utilisateur:utilisateur_list')
    else:
        form = CustomUserForm(instance=utilisateur)
    return render(request, 'utilisateur/utilisateur_form.html', {'form': form})

@login_required
def utilisateur_delete(request, pk):
    utilisateur = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        utilisateur.delete()
        return redirect('utilisateur:utilisateur_list')
    return render(request, 'utilisateur/utilisateur_confirm_delete.html', {'utilisateur': utilisateur})





# inscription:
#-------------

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utilisateur:login')  # redirigez vers la page de connexion ou une autre page appropriée
    else:
        form = CustomUserCreationForm()
    return render(request, 'utilisateur/signup.html', {'form': form})