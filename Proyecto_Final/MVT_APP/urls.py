from django.urls import path
from MVT_APP.views import *
from authentication_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("inicio/", homepage, name="homepage"),
    path("Libros/", libros, name="libros"),
    path("autores/", autores, name="autores"),
    path("editoriales/", editoriales, name="editoriales"),
    path("editoriales/buscar/resultados/", resultados_busqueda_editoriales, name="editorial_resultados"),
    path("libros/buscar/resultados/", resultados_busqueda_libros, name="libro_resultados"),
    path("autores/buscar/resultados/", resultados_busqueda_autores, name="autor_resultados"),
    path("auth/login/", iniciar_sesion, name="auth-login"),
    path("registro/", registrar_usuario, name="auth-register"),
    path("logout/", cerrar_sesion, name="auth-logout"),
    path("perfil/editar/", editar_perfil, name="auth-editar-perfil"),
    path("perfil/avatar/", agregar_avatar, name="auth-avatar"),    
    path("editoriales/borrar/<pk>", EditorialDelete.as_view(), name="editorial-delete"),
    path("editoriales/actualizar/<pk>", EditorialEdit.as_view(), name="editorial-edit"),
    path("editoriales/listar/", EditorialList.as_view(), name="editorial-list"),
    path("editoriales/detalle/<pk>", EditorialDetail.as_view(), name="editorial-detail"),
    path("libros/borrar/<pk>", LibroDelete.as_view(), name="libro-delete"),
    path("libros/actualizar/<pk>", LibroEdit.as_view(), name="libro-edit"),
    path("libros/listar/", LibroList.as_view(), name="libro-list"),
    path("libros/detalle/<pk>", LibroDetail.as_view(), name="libro-detail"),
    path("autores/borrar/<pk>", AutorDelete.as_view(), name="autor-delete"),
    path("autores/actualizar/<pk>", AutorEdit.as_view(), name="autor-edit"),
    path("autores/listar/", AutorList.as_view(), name="autor-list"),
    path("autores/detalle/<pk>", AutorDetail.as_view(), name="autor-detail"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)