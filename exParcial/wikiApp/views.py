from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistaprincipal(request):
    return render(request,'vistaprincipal.html')

def vista_crear_nuevo_tema(request):
    return render(request,'vista_crear_nuevo_tema.html')

def vista_crear_nuevo_articulo(request):
    return render(request,'vista_crear_nuevo_articulo.html')

def vista_articulo_por_tema(request):
    return render(request,'vista_articulo_por_tema.html')

def vista_de_articulos(request):
    return render(request,'vista_de_articulos.html')

def vista_de_busqueda(request):
    return render(request,'vista_de_busqueda.html')

