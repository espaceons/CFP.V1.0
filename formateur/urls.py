
from django.urls import path

from cf.views import index

app_name = 'formateur'

urlpatterns = [
    path('', index, name='index'),
]
