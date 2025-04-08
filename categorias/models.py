from django.db import models

class Categoria(models.Model):
    #Aqui van los atributos de mi clase
    nombre = models.CharField(max_length=100)
    #Los campos URLFields limitan los caracteres a 200 por defecto
    imagen = models.URLField()

    def __str__(self):
        return self.nombre
    
    