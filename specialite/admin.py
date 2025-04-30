# specialite/admin.py
from django.contrib import admin
from specialite.models import Cours, Specialite

admin.site.register(Specialite)
admin.site.register(Cours)