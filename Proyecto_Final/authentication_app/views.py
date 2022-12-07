from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from authentication_app.forms import *
from authentication_app.models import *

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


@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        # * cargar informacion en el formulario
        formulario = UserEditForm(request.POST)

        # ! validacion del formulario
        if formulario.is_valid():
            data = formulario.cleaned_data

            # * actualizacion del usuario con los datos del formulario
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
            return redirect("homepage")
        else:
            return render(request, "editar_perfil.html", {"form": formulario, "errors": formulario.errors})
    else:
        # * crear formulario vacio
        formulario = UserEditForm(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})

    return render(request, "editar_perfil.html", {"form": formulario})


@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        formulario = AvatarForm(request.POST, files=request.FILES)
        print(request.FILES, request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("homepage")
        else:
            return render(request, "agregar_avatar.html", {"form": formulario, "errors": formulario.errors })
    formulario = AvatarForm()

    return render(request, "agregar_avatar.html", {"form": formulario})