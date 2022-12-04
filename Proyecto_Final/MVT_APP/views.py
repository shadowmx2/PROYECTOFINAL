from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from MVT_APP.forms import *
from MVT_APP.models import *
 

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage.html', {'familia':'1'})    

    
@login_required
def libros(request):
    return render(request, 'libros.html', {'familia':'1'})    

@login_required
def autores(request):
    return render(request, 'autores.html', {'familia':'1'})    

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
        formulario = LibroFormulario(request.POST)
 
        if formulario.is_valid():
            
            data = formulario.cleaned_data

            libro = Libro(titulo=data["titulo"], fecha_Publicacion=data["fecha_Publicacion"], genero=data["genero"],autor=data["autor"],editorial=data["editorial"], calificacion=data["calificacion"])

            libro.save()
    formulario = LibroFormulario()    
    contexto = {"formulario": formulario}
    return render(request, "libros.html", contexto)

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


  

def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                return render(request, "login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "login.html", {"form": formulario, "errors": errors})
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("homepage")

def registrar_usuario(request):
     
    if request.method =="POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("homepage")
        else:
            return render(request, "register.html", { "formulario": formulario, "errors": formulario.errors})

    formulario  = UserRegisterForm()
    return render(request, "register.html", { "formulario": formulario})