from django.http import HttpResponse
# Request: realizar peticiones
# HTTPResponse: enviar respuestas

def welcome(request):
    return HttpResponse("Hola Mundo")