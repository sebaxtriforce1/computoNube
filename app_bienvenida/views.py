from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenida(request):
    return HttpResponse("<h1>Sebastian Ocampo Carmona</h1><h2><a href='mensajes'>Mensajes</a></h2>")