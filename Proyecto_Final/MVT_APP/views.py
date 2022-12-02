from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from MVT_APP.forms import *
from MVT_APP.models import *
import datetime

def homepage(request):
    return render(request, 'homepage.html', {'familia':'1'})    

    

def libros(request):
    return render(request, 'libros.html', {'familia':'1'})    

def autores(request):
    return render(request, 'autores.html', {'familia':'1'})    

def editoriales(request):
    if request.method == "POST":
        formulario = EditorialFormulario(request.POST)
 
        if formulario.is_valid():
             
            data = formulario.cleaned_data

            editorial = Editorial(nombre=data["nombre"], fecha_creacion=data["fecha_creacion"], pais=data["pais"])

            editorial.save()
    formulario = EditorialFormulario()    
    contexto = {"formulario": formulario}
    return render(request, "editoriales.html", contexto)


def resultados_busqueda_editoriales(request):
    nombre = request.GET["nombre_editorial"]

    editoriales = Editorial.objects.filter(nombre__icontains=nombre)
    return render(request, "resultadoeditorial.html", {"editoriales": editoriales})


def libros(request):
    if request.method == "POST":
        formulario = LibroFormulario(request.POST)
 
        if formulario.is_valid():
            
            data = formulario.cleaned_data

            libro = Libro(titulo=data["titulo"], fecha_Publicacion=data["fecha_Publicacion"], genero=data["genero"],autor=data["autor"],editorial=data["editorial"], calificacion=data["calificacion"])

            libro.save()
    formulario = LibroFormulario()    
    contexto = {"formulario": formulario}
    return render(request, "libros.html", contexto)


def resultados_busqueda_libros(request):
    titulo = request.GET["titulo_libro"]

    libros= Libro.objects.filter(titulo__icontains=titulo)
    return render(request, "resultadoslibro.html", {"libros": libros})

def autores(request):
    if request.method == "POST":
        formulario = AutorFormulario(request.POST)
 
        if formulario.is_valid():
             
            data = formulario.cleaned_data

            editorial = Autor(nombre=data["nombre"], apellido=data["apellido"], fecha_nacimiento=data["fecha_nacimiento"], edad=data["edad"], email=data["email"], nacionalidad=data["nacionalidad"])

            editorial.save()
    formulario = AutorFormulario()    
    contexto = {"formulario": formulario}
    return render(request, "autores.html", contexto)

def resultados_busqueda_autores(request):
    autor = request.GET["nombre"]

    autores= Autor.objects.filter(nombre__icontains=autor)
    return render(request, "resultadoautores.html", {"autores": autores})