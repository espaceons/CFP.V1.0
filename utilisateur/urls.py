from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'utilisateur'

urlpatterns = [
    path('', views.utilisateur_list, name='utilisateur_list'),
    path('create/', views.utilisateur_create, name='utilisateur_create'),
    path('<int:pk>/update/', views.utilisateur_update, name='utilisateur_update'),
    path('<int:pk>/delete/', views.utilisateur_delete, name='utilisateur_delete'),
    
    path('login/', auth_views.LoginView.as_view(template_name='utilisateur/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
