from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EditorialFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_creacion = forms.DateField()
    pais = forms.CharField()

class AutorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    nacionalidad = forms.CharField()

class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    fecha_Publicacion = forms.DateField() 
    genero = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    calificacion = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    username= forms.CharField(label="Usuario")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "last_name", "first_name", "password1", "password2"]


class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput, required=False)
   
    class Meta:
        model = User
        fields = ["email", "last_name", "first_name"]

        # ? La siguiente linea elimina cualquier mensaje de ayuda en los campos
        # ?help_texts = { k: "" for k in fields }
        help_texts = { "email": "Indica un correo electronico que uses habitualmente", "first_name": "", "last_name": "", "password1": ""}


class AvatarForm(forms.Form):
    imagen = forms.ImageField()
