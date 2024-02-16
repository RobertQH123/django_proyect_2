from django.http import HttpResponse
from django.shortcuts import render
from Academico.models import Curso

# Create your views here.


def home(request):
    cur = Curso.objects.all()
    return render(request, "cursoAllTemplate.html",{"cursos":cur})
