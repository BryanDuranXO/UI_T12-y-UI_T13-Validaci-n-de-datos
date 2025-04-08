from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewset, crud

#definir un router
router = SimpleRouter()
#registrar las url del sistema
router.register(r'api',AlumnoViewset) 


#ProductoViewset:
#ip:8000/productos/api/ <--- Get de todo
#ip:8000/productos/api/{id} <--- Get, POST, PUT, DELETE de uno

urlpatterns=[
    path('', include(router.urls)),
    path('alumno/crud/', crud, name='crud'),
]
