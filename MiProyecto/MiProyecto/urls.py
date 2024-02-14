"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiProyecto.views import welcome, ageCategory, getCurrentMoment, contentHTML, firstTemplate, parametersTemplate, loadedTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenido/', welcome),
    path('categoriaEdad/<int:age>', ageCategory),
    path('obtenerMomentoActual/', getCurrentMoment),
    path('contenidoHTML/<str:name>/<int:age>', contentHTML),
    path('primeraPlantilla/', firstTemplate),
    path('parametrosPlantilla/', parametersTemplate),
    path('loadedTemplate/', loadedTemplate),

]
