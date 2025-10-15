from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='empleados_fotos/')

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.id_empleado.nombre} - {self.fecha}"
