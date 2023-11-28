from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Equipo, Jugador, Camiseta
from .forms import EquipoForm, JugadorForm, CamisetaForm

def equipo_nuevo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipo_nuevo')
    else:
        form = EquipoForm()
    return render(request, 'tu_aplicacion/equipo_nuevo.html', {'form': form})
