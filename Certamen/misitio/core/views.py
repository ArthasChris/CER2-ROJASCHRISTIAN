from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import Comunicado, Entidad

def lista_comunicados(request):
    comunicados = Comunicado.objects.all()
    return render(request, 'core/card.html', {'comunicados': comunicados})

def index(request, entidad_id=None):
    entidades = Entidad.objects.all()
    comunicados = []
    print("Vista mostrar_comunicados se está ejecutando")
    if entidad_id:
        # Si se selecciona una entidad, recupera los comunicados relacionados
        entidad = Entidad.objects.get(id=entidad_id)
        comunicados = Comunicado.objects.filter(entidad=entidad)
        print("hola mundo")

    return render(request, 'core/index.html', {'entidades': entidades, 'comunicados': comunicados})

