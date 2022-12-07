from django import forms
 


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
    #portada = forms.ImageField() 
    imagen = forms.ImageField()

 
