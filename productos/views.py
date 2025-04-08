from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Producto
from .serializers import ProductoSerializer
from .forms import productoForm
from django.shortcuts import render


def agregar(request):
    form = productoForm()
    return render(
        request,
        'agregar.html',
        {'form':form},
        status=200
    )

class ProductoViewset(viewsets.ModelViewSet):
    #conjunto de querys de la BD
    queryset = Producto.objects.all()

    #saber como empaquetar y enviar la info
    serializer_class = ProductoSerializer

    #saber como voy a renderizar las respuestas
    renderer_classes = [JSONRenderer]

    http_method_names = ['GET', 'POST'] #metodos especificos 