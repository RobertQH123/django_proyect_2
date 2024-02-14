from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader

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

def contentHTML(request,name,age):
    content = """
    <html>
    <body>
    <p>Nombre: %s / Edad: %s</p>
    </body>
    </html>
    """%(name,age)
    return HttpResponse(content)

def firstTemplate(request):
    templateOpen = open("C:/djangotutorial/django_proyect_2/MiProyecto/MiProyecto/templates/firstTemplate.html")
    template = Template(templateOpen.read())
    templateOpen.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def parametersTemplate(request):
    language = ["python","java","PHP","javascript","ruby","c++"]
    templateOpen = open("C:/djangotutorial/django_proyect_2/MiProyecto/MiProyecto/templates/parametersTemplate.html")
    template = Template(templateOpen.read())
    templateOpen.close()
    context = Context({"name":"robert","language": language})
    document = template.render(context)
    return HttpResponse(document)