from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("HOLA DJANGO - CODER")

def saludo2(request):
    return HttpResponse("HOLA DJANGO - CODER")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documento_de_texto = f"Hoy es día: {dia}"
    return HttpResponse(documento_de_texto)
