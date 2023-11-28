from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .forms import EquipoForm

def equipo_nuevo(request):
    try:
        if request.method == "POST":
            form = EquipoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Equipo creado exitosamente.')
                return redirect('lista_equipos')  
            else:
                messages.error(request, 'Hubo un error en el formulario. Corrige los errores e intenta nuevamente.')
        else:
            form = EquipoForm()
    except ValidationError as e:
        messages.error(request, f'Error de validación del formulario: {str(e)}')
    
    return render(request, 'ProyectoFinal/equipo_nuevo.html', {'form': form})
