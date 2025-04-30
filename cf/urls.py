
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from cf.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('utilisateur/', include('utilisateur.urls')),
    path('specialite/', include('specialite.urls')),
    path('stagiaire/', include('stagiaire.urls')),
    path('formateur/', include('formateur.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
