from django.contrib import admin
from . models import Empresas

# Abaixo eu crio o class "Empresas" do banco de dados, dentro do admin do django.
admin.site.register(Empresas)