from django.shortcuts import render
from .models import Sede, usuarios_contactados, usuarios_gimnasio
from .forms import UsuarioFormulario, UserEditForm, UserEditForm_password, UsuarioFormularioSede
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Redirecciones básicas


def inicio(req):  # redirecciona a user/inicio/

    return render(req, 'index.html', {})


def sobre_nosotros(req):  # redirecciona a user/about/

    return render(req, 'about.html', {})


def contacto(req):  # redirecciona a user/contacto/

    return render(req, 'contact.html', {})

# Views sin permisos


def buscar(req):
    '''
    Funcion para buscar sedes dentro de user/sedes/
    '''

    try:

        if req.GET["tipoDeSede"]:

            tipo_de_sede = req.GET["tipoDeSede"]
            lista_sedes = Sede.objects.filter(
                tipo_gimnasio__icontains=tipo_de_sede)

        else:
            lista_sedes = Sede.objects.filter(
                tipo_gimnasio__icontains=" ")  # no pone nada

        return render(req, 'sedes.html', {'ListaSede': lista_sedes})

    except:
        return render(req, "usuario_registrado.html", {"message": "Error 404 - Acceso no autorizado"})


def registrar(req):
    '''
    Funcion para registrar contactos de usuarios que buscan informacion
    '''

    miFormulario = req.POST

    if miFormulario:

        data = miFormulario.dict()

        nuevo_usuario = usuarios_contactados(nombre=data.get('NombreUsuario'), correo=data.get(
            'CorreoUsuario'), Telefono=data.get('TelefonoUsuario'), Mensaje=data.get('ComentarioUsuarios'))
        nuevo_usuario.save()

    return render(req, 'usuario_registrado.html', {'message': 'Nos comunicaremos contigo pronto'})


def usuario_nuevo(req):
    '''
    Funcion con formulario para la creacion de nuevos usuarios que a la vez crea usuarios de sistema
    '''

    if req.method == 'POST':

        info = req.POST

        miFormulario = UsuarioFormulario({
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'correo': info['correo'],
            'Telefono': info['Telefono'],
        })

        userform = UserCreationForm({
            "username": info["username"],
            "password1": info["password1"],
            "password2": info["password2"],
        })

        if miFormulario.is_valid() and userform.is_valid():

            data = miFormulario.cleaned_data
            data.update(userform.cleaned_data)

            user = User(username=data["username"], first_name=data['nombre'],
                        last_name=data['apellido'], email=data['correo'])

            user.set_password(data["password1"])
            user.save()

            nuevo_profesor = usuarios_gimnasio(
                nombre=data['nombre'], apellido=data['apellido'], correo=data['correo'], Telefono=data['Telefono'], user_id=user)
            nuevo_profesor.save()

            return render(req, "usuario_registrado.html", {"message": f"Usuario {data['username']} creado con éxito!"})

        else:

            return render(req, "usuario_registrado.html", {"message": "Datos inválidos"})

    else:

        miFormulario = UsuarioFormulario()
        userForm = UserCreationForm()

        return render(req, "usuario_nuevo.html", {"miFormulario": miFormulario, "userForm": userForm})


def login_view(req):
    '''
    Funcion de formulario para autenticar usuarios registrados a la plataforma
    '''

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "index.html", {"message": f"Bienvenido {usuario}"})

            else:
                return render(req, "usuario_registrado.html", {"message": "Datos erroneos"})

        else:

            return render(req, "usuario_registrado.html", {"message": "Datos inválidos"})

    else:

        miFormulario = AuthenticationForm()

        return render(req, "login.html", {"miFormulario": miFormulario})


def sedes(req):
    '''
    Funcion extrae toda la informacion de sedes
    '''

    lista_sedes = Sede.objects.all()

    return render(req, 'sedes.html', {'ListaSede': lista_sedes})

# Views para usuarios logueados


@login_required
def editar_perfil(req):
    '''
    Funcion que edita el propio perfil del usuario logueado
    '''

    usuario = req.user

    if req.method == 'POST':

        info = req.POST

        Sedeformulario = UsuarioFormularioSede({
            'sede': info['sede'],
        })

        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid() and Sedeformulario.is_valid():

            data = miFormulario.cleaned_data
            data.update(Sedeformulario.cleaned_data)

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            perfil_editado = usuarios_gimnasio.objects.get(
                user_id_id=req.user.id)
            perfil_editado.nombre = data['first_name']
            perfil_editado.apellido = data['last_name']
            perfil_editado.correo = data['email']
            perfil_editado.sede = data['sede']

            usuario.save()
            perfil_editado.save()

            return render(req, "usuario_registrado.html", {"message": "Datos actualizado con éxito"})

        else:

            return render(req, "usuario_registrado.html", {"message": "Datos erroneos"})

    else:

        miFormulario = UserEditForm(instance=req.user)
        perfil_editado = usuarios_gimnasio.objects.get(user_id_id=req.user.id)
        sede_id = perfil_editado.sede

        sedeUsuario = UsuarioFormularioSede(initial={'sede': sede_id})

        return render(req, "editar_perfil.html", {"miFormulario": miFormulario, "misedeFormulario": sedeUsuario})


@login_required
def editar_contrasena(req):

    usuario = req.user

    if req.method == 'POST':

        info = req.POST

        Sedeformulario = UsuarioFormularioSede({
            'sede': info['sede'],
        })

        miFormulario = UserEditForm_password(req.POST, instance=req.user)

        if miFormulario.is_valid() and Sedeformulario.is_valid():

            data = miFormulario.cleaned_data
            data.update(Sedeformulario.cleaned_data)

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            perfil_editado = usuarios_gimnasio.objects.get(
                user_id_id=req.user.id)
            perfil_editado.nombre = data['first_name']
            perfil_editado.apellido = data['last_name']
            perfil_editado.correo = data['email']
            perfil_editado.sede = data['sede']

            usuario.set_password(data["password1"])
            usuario.save()

            # hace que el usuario se desloquee luego de cambiar el password
            logout(req)

            return render(req, "usuario_registrado.html", {"message": "Contraseña actualizada. Has sido deslogueado, vuelve a ingresar"})

        else:

            return render(req, "usuario_registrado.html", {"message": "Contraseñas diferentes"})

    else:

        miFormulario = UserEditForm_password(instance=req.user)

        perfil_editado = usuarios_gimnasio.objects.get(user_id_id=req.user.id)
        sede_id = perfil_editado.sede

        sedeUsuario = UsuarioFormularioSede(initial={'sede': sede_id})

        return render(req, "editar_contrasena.html", {"miFormulario": miFormulario, "misedeFormulario": sedeUsuario})

# Views para usuarios Staff


@staff_member_required
def lista_usuarios(req):

    usuarios_lista = usuarios_gimnasio.objects.all()

    print(usuarios_lista)

    return render(req, 'lista_usuarios.html', {'UsuarioLista': usuarios_lista})


@staff_member_required
def buscar_usuarios(req):

    if req.GET["usuario_buscado"]:

        usuario_buscado = req.GET['usuario_buscado']
        lista_usarios = usuarios_gimnasio.objects.filter(
            nombre__icontains=usuario_buscado)
    else:
        lista_usarios = usuarios_gimnasio.objects.filter(
            nombre__icontains=" ")  # no pone nada

    return render(req, 'lista_usuarios.html', {'UsuarioLista': lista_usarios})


@method_decorator(staff_member_required, name='dispatch')
class SedeDetail(DetailView):

    model = Sede
    template_name = 'sede_detail.html'
    context_object_name = "sede"


@method_decorator(staff_member_required, name='dispatch')
class SedeUpdate(UpdateView):

    model = Sede
    template_name = 'sede_detail.html'
    fields = ('__all__')
    success_url = "/user/sedes/"
    context_object_name = "sede"


@method_decorator(staff_member_required, name='dispatch')
class SedeDelete(DeleteView):

    model = Sede
    template_name = 'sede_delete.html'
    success_url = "/user/sedes/"
    context_object_name = "sede"


@method_decorator(staff_member_required, name='dispatch')
class SedeCreate(CreateView):

    model = Sede
    template_name = 'sede_create.html'
    fields = ('__all__')
    success_url = "/user/sedes/"
