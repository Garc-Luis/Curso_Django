from django.http import HttpResponse

def saludos(request):
    return HttpResponse('Hola Mundo.')

def despedida(request):
    return HttpResponse('Hasta luego Amigos.')