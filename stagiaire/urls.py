
from django.urls import path

from cf.views import index

app_name = 'stagiaire'

urlpatterns = [
    path('', index, name='index'),
]
