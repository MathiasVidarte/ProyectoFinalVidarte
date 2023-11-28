from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Equipo
from .forms import EquipoForm

def equipo_nuevo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo creado exitosamente.')
            return redirect('lista_equipos')
        else:
            messages.error(request, 'Hubo un error en el formulario. Por favor, corrige los errores e intenta nuevamente.')
    else:
        form = EquipoForm()

    return render(request, 'tu_aplicacion/equipo_nuevo.html', {'form': form})
