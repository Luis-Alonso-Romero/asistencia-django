from .models import Empleado, Asistencia
from .forms import EmpleadoForm, AsistenciaForm
from django.shortcuts import render, redirect, get_object_or_404

# ---------------------- EMPLEADOS ----------------------
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/form.html', {'form': form})

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/form.html', {'form': form})

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    return redirect('lista_empleados')


# ---------------------- ASISTENCIAS ----------------------
def lista_asistencias(request):
    asistencias = Asistencia.objects.select_related('id_empleado').all()
    return render(request, 'asistencias/lista.html', {'asistencias': asistencias})

def crear_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asistencias')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencias/form.html', {'form': form})

def editar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return redirect('lista_asistencias')
    else:
        form = AsistenciaForm(instance=asistencia)
    return render(request, 'asistencias/form.html', {'form': form})

def eliminar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    asistencia.delete()
    return redirect('lista_asistencias')
