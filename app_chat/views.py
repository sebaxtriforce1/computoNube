from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Carreras, Persona, Mensajes

# Create your views here.

def consultar(request):
    mensajes = Mensajes.objects.select_related('persona', 'persona__carrera').all().order_by('id')

    html = "<!DOCTYPE html><html><head><title>Mensajes</title></head><body>"

    for mensaje in mensajes:
        nombre_completo = f"<b>{mensaje.persona.nombre} {mensaje.persona.ap_pat} {mensaje.persona.ap_mat}</b>"
        carrera = f"<span style='color: blue;'>{mensaje.persona.carrera.nombre}</span>"

        html += f"""
            <p>
                Mensaje: {mensaje.txt_mensaje} <br>
                Nombre: {nombre_completo} <br>
                Carrera: {carrera}
            </p>
        """

    html += "</body></html>"
    return HttpResponse(html)