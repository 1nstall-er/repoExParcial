from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import temaWiki,articuloWiki

listaTemas = []

# Create your views here.

def vistaprincipal(request):
    return render(request,'vistaprincipal.html', {
        'listaTemas':listaTemas
    })

def vista_crear_nuevo_tema(request):
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        listaTemas.append(nombreTema)
    return render(request,'vista_crear_nuevo_tema.html', {
        'listaTemas':listaTemas
    })

def vista_crear_nuevo_articulo(request):
    return render(request,'vista_crear_nuevo_articulo.html', {
        'listaTemas':listaTemas
    })

def vista_articulo_por_tema(request):
    return render(request,'vista_articulo_por_tema.html', {
        'listaTemas':listaTemas
    })

def vista_de_articulos(request):
    return render(request,'vista_de_articulos.html', {
        'listaTemas':listaTemas
    })

def vista_de_busqueda(request):
    return render(request,'vista_de_busqueda.html', {
        'listaTemas':listaTemas
    })

