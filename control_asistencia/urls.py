from django.urls import path
from . import views

urlpatterns = [
    # EMPLEADOS
    path('', views.lista_empleados, name='lista_empleados'),
    path('empleado/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleado/editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('empleado/eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),

    # ASISTENCIAS
    path('asistencias/', views.lista_asistencias, name='lista_asistencias'),
    path('asistencia/crear/', views.crear_asistencia, name='crear_asistencia'),
    path('asistencia/editar/<int:id>/', views.editar_asistencia, name='editar_asistencia'),
    path('asistencia/eliminar/<int:id>/', views.eliminar_asistencia, name='eliminar_asistencia'),
]
