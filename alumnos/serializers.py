from rest_framework import serializers
from .models import Alumno

#es una clase quw actua sobre un modelo

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__' # <-- todos los campos

    