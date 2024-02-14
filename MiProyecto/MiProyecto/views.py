from django.http import HttpResponse
import datetime
# Request: realizar peticiones
# HTTPResponse: enviar respuestas

def welcome(request):
    return HttpResponse("Hola Mundo")

def ageCategory(request, age):
    if age >= 18:
        if age >= 60:
            category = "Tercera edad"
        else:
            category = "Adultez"
    else:
        if age < 10:
            category = "Infancia"
        else:
            category = "Adolecencia"
    
    result = "<h1>Categoria de edad: %s</h1>" %category
    return HttpResponse(result)

def getCurrentMoment(request):
    result = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(result)