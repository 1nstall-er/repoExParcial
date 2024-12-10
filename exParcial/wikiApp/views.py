from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import temaWiki,articuloWiki



# Create your views here.

def vistaprincipal(request):
    return render(request,'vistaprincipal.html', {
        'listaTemas':temaWiki.objects.all()
    })

def vista_crear_nuevo_tema(request):
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        temaWiki.objects.create(
            nombreTema=nombreTema,
            descripcionTema=descripcionTema,
        )
    return render(request,'vista_crear_nuevo_tema.html', {
        'listaTemas':temaWiki.objects.all()
    })

def vista_crear_nuevo_articulo(request):
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        tema = request.POST.get('tema')
        temaObj = temaWiki.objects.get(id=tema)
        articuloWiki.objects.create(
            tituloArticulo=tituloArticulo,
            contenidoArticulo=contenidoArticulo,
            temaR=temaObj,
        )
    return render(request,'vista_crear_nuevo_articulo.html', {
        'listaTemas':temaWiki.objects.all(),
    })

def vista_articulo_por_tema(request, idTema):
    temainfo = temaWiki.objects.get(id=idTema)
    listaArticulos = temainfo.articulowiki_set.all()
    return render(request,'vista_articulo_por_tema.html', {
        'objTema':temainfo,
        'listaTemas':temaWiki.objects.all(),
        'listaArticulos':listaArticulos,
    })

def vista_de_articulos(request, idArticulo):
    articuloinfo = articuloWiki.objects.get(id=idArticulo)
    return render(request,'vista_de_articulos.html', {
        'objArticulo':articuloinfo,
        'listaTemas':temaWiki.objects.all(),
    })

def vista_de_busqueda(request):
    return render(request,'vista_de_busqueda.html', {
        'listaTemas':temaWiki.objects.all()
        
    })

