from django.shortcuts import render
from .models import Sede, usuarios_contactados, usuarios_gimnasio
from .forms import UsuarioFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Create your views here.


def inicio(req):

    return render(req, 'index.html', {})


def sobre_nosotros(req):

    return render(req, 'about.html', {})


#def servicios(req):
#
#    return render(req, 'service.html', {})


def contacto(req):

    return render(req, 'contact.html', {})

def sedes(req):

    lista_sedes = Sede.objects.all()

    #print(lista_sedes)

    return render(req, 'sedes.html', {'ListaSede' : lista_sedes})


def buscar(req):

    if req.GET["tipoDeSede"]:

        tipo_de_sede = req.GET["tipoDeSede"]
        lista_sedes =  Sede.objects.filter(tipo_gimnasio__icontains=tipo_de_sede)

        

    else:
        lista_sedes =  Sede.objects.filter(tipo_gimnasio__icontains=" ") #no pone nada
    
    return render(req, 'sedes.html', {'ListaSede' : lista_sedes})


def registrar(req):

    miFormulario = req.POST

    if miFormulario:

        data = miFormulario.dict()

        nuevo_usuario = usuarios_contactados(nombre = data.get('NombreUsuario'), correo = data.get('CorreoUsuario'), Telefono = data.get('TelefonoUsuario') , Mensaje = data.get('ComentarioUsuarios'))
        nuevo_usuario.save()

    return render(req, 'usuario_registrado.html', {'NombreUsuario' : data.get('NombreUsuario')})
    

def usuario_nuevo(req):

    if req.method == 'POST':

        info = req.POST

        miFormulario = UsuarioFormulario({
            'nombre' : info['nombre'],
            'correo' : info['correo'],
            'Telefono' : info['Telefono'],
        })

        userform = UserCreationForm({
            "username": info["username"],
            "password1": info["password1"],
            "password2": info["password2"],
        })

        #miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid() and userform.is_valid():

            data = miFormulario.cleaned_data
            data.update(userform.cleaned_data)

            user = User(username=data["username"])
            user.set_password(data["password1"])
            user.save()

            nuevo_profesor = usuarios_gimnasio(nombre=data['nombre'], correo=data['correo'], Telefono=data['Telefono'],user_id=user)
            nuevo_profesor.save()


            return render(req, "usuario_registrado.html", {"message": f"Usuario {data['username']} creado con éxito!"})
    
        else:


            return render(req, "usuario_registrado.html", {"message": "Datos inválidos"}) #hacer un HTML de error 
  
    else:

        miFormulario = UsuarioFormulario()
        userForm = UserCreationForm()

        return render(req, "usuario_nuevo.html", {"miFormulario": miFormulario , "userForm": userForm})

