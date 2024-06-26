"""
URL configuration for proyecto_gym project.

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
from django.urls import path
from .views import inicio, contacto, sobre_nosotros, sedes, buscar, registrar,usuario_nuevo, login_view, editar_perfil, editar_contrasena
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('editar_perfil/', editar_perfil, name= 'EditarPerfil'),
    path('inicio/', inicio, name= 'inicio'),
    path('sedes/', sedes, name= 'sedes'),
    path('about/', sobre_nosotros, name= 'sobre'),
    path('contacto/', contacto, name= 'contacto'),
    path('sedes_resultado/', buscar, name= 'buscar_sede'),
    path('contacto_registrado/', registrar, name= 'ContactoRegistrado'),
    path('registro/', usuario_nuevo, name= 'UsuarioRegistrado'),
    path('login/', login_view, name='Login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='Logout'),
    path('editar_contrasena/', editar_contrasena, name='editarcontrasena'),
    

    

]
