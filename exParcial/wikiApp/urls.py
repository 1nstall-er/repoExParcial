from django.urls import path
from . import views

app_name='wikiApp'

urlpatterns = [
    path('',views.vistaprincipal,name='vistapricipal'),
    path('vista_crear_nuevo_tema',views.vista_crear_nuevo_tema,name='vista_crear_nuevo_tema'),
    path('vista_crear_nuevo_articulo',views.vista_crear_nuevo_articulo,name='vista_crear_nuevo_articulo'),
    path('vista_articulo_por_tema',views.vista_articulo_por_tema,name='vista_articulo_por_tema'),
    path('vista_de_articulos',views.vista_de_articulos,name='vista_de_articulos'),
    path('vista_de_busqueda',views.vista_de_busqueda,name='vista_de_busqueda'),
]
