from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #nombre=request.GET.get("nombre") or "mundo"
    #return HttpResponse(f"Hola {nombre}!")
    nombre="marte"
    return render(request, "base.html", {"nombre":nombre})