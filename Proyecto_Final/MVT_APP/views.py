from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from MVT_APP.forms import *
from MVT_APP.models import *
from authentication_app.models import Avatar
 
 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView,  UpdateView, DeleteView


def homepage(request):
    

    return render(request, 'homepage.html', avatar_mostrar(request))    

    
def avatar_mostrar(request):
    if request.user.is_authenticated:            
        ava = Avatar.objects.filter(user= request.user.id)
        if ava.count()> 0:
            imagen_model = ava.order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        else:
            imagen_url=""
    else:
        imagen_url = ""
    return {"imagen_url": imagen_url}

@login_required
def libros(request):
    return render(request, 'libros.html')    

@login_required
def autores(request):
    return render(request, 'autores.html')    

@login_required
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

@login_required
def resultados_busqueda_editoriales(request):
    nombre = request.GET["nombre_editorial"]

    editoriales = Editorial.objects.filter(nombre__icontains=nombre)
    return render(request, "resultadoeditorial.html", {"editoriales": editoriales})

@login_required
def libros(request):
    if request.method == "POST":
        formulario = LibroFormulario(request.POST,files=request.FILES)
 
        if formulario.is_valid():
            
            data = formulario.cleaned_data

            libro = Libro(titulo=data["titulo"], fecha_Publicacion=data["fecha_Publicacion"], genero=data["genero"],autor=data["autor"],editorial=data["editorial"], calificacion=data["calificacion"],imagen=data["imagen"])

            libro.save()
    formulario = LibroFormulario()    
    #contexto = {"formulario": formulario}
    return render(request, "libros.html",  {"formulario": formulario})

@login_required
def resultados_busqueda_libros(request):
    titulo = request.GET["titulo_libro"]

    libros= Libro.objects.filter(titulo__icontains=titulo)
    return render(request, "resultadoslibro.html", {"libros": libros})

@login_required
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

@login_required
def resultados_busqueda_autores(request):
    autor = request.GET["nombre"]

    autores= Autor.objects.filter(nombre__icontains=autor)
    return render(request, "resultadoautores.html", {"autores": autores})




class EditorialDelete(DeleteView):

    model = Editorial
    success_url = "/editoriales/"

class EditorialEdit(UpdateView):

    model = Editorial
    success_url = "/editoriales/"
    fields = ["fecha_creacion", "pais"]

class EditorialList(LoginRequiredMixin, ListView):

    model = Editorial
    template_name = "list_editorial.html"


class EditorialDetail(DetailView):

    model = Editorial
    template_name = "detail_editorial.html"


    

class LibroDelete(DeleteView):

    model = Libro
    success_url = "/Libros/"

class LibroEdit(UpdateView):

    model = Libro
    success_url = "/Libros/"
    fields = ["fecha_Publicacion", "titulo","genero","autor", "editorial","calificacion","imagen"]

class LibroList(LoginRequiredMixin, ListView):

    model = Libro
    template_name = "list_libro.html"


class LibroDetail(DetailView):

    model = Libro
    template_name = "detail_libro.html"


class AutorDelete(DeleteView):

    model = Autor
    success_url = "/autores/"

class AutorEdit(UpdateView):

    model = Autor
    success_url = "/autores/"
    fields = ["fecha_nacimiento", "nombre","apellido","edad", "email","nacionalidad"]

class AutorList(LoginRequiredMixin, ListView):

    model = Autor
    template_name = "list_autor.html"


class AutorDetail(DetailView):

    model = Autor
    template_name = "detail_autor.html"

     
