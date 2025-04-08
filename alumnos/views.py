from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Alumno
from .serializers import AlumnoSerializer
from django.shortcuts import render, redirect
from .forms import AlumnoForm


class AlumnoViewset(viewsets.ModelViewSet):
    #conjunto de querys de la BD
    queryset = Alumno.objects.all()

    #saber como empaquetar y enviar la info
    serializer_class = AlumnoSerializer

    #saber como voy a renderizar las respuestas
    renderer_classes = [JSONRenderer]


def crud(request):
    form = AlumnoForm()
    return render(request, 'Miranda_Bryan.html', {'form': form})
