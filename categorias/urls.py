from django.urls import path
from .views import *

urlpatterns = [
    path('agregar/', agregar_categorias, name='agregar'),
    path('agregar2/', agregar_categorias2, name='agregar'),
    path('json/', ver_categorias, name='lista'),
    path('', index, name='home'),
    path('api/get/', lista_categorias, name='ver'),
    path('api/post/', registrar_categorias, name='registrar')
]