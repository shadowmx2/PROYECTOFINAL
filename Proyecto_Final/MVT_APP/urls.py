from django.urls import path
from MVT_APP.views import *

urlpatterns = [
    path("inicio/", homepage, name="homepage"),
    path("Libros/", libros, name="libros"),
    path("autores/", autores, name="autores"),
    path("editoriales/", editoriales, name="editoriales"),
    path("editoriales/buscar/resultados/", resultados_busqueda_editoriales, name="editorial_resultados"),
    path("libros/buscar/resultados/", resultados_busqueda_libros, name="libro_resultados"),
    path("autores/buscar/resultados/", resultados_busqueda_autores, name="autor_resultados"),
    path("login/", iniciar_sesion, name="auth-login"),
    path("registro/", registrar_usuario, name="auth-register"),
]
