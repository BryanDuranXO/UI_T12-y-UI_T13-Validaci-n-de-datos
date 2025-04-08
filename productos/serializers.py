from rest_framework import serializers
from .models import Producto

#es una clase quw actua sobre un modelo

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' # <-- todos los campos

    