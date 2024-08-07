from django.shortcuts import render
from .models import Empresas


def cadastrar_empresa(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_empresa.html', {'tempo_existencia': Empresas.tempo_existencia_choices, 'areas': Empresas.area_choices})
