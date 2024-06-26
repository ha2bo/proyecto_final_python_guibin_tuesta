from django import forms
from .models import Sede, usuarios_gimnasio
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class MiFormulario(forms.Form):
    sedes_select = forms.ModelMultipleChoiceField(
    queryset=Sede.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    )



class UsuarioFormulario(forms.ModelForm):

  class Meta:
    model= usuarios_gimnasio
    #fields=('__all__')
    fields=["nombre", 'apellido', 'correo', "Telefono"]



class UserEditForm(UserChangeForm):

  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
  )

  class Meta:
    model=User
    fields=["email", "first_name", "last_name"]

  

class UserEditForm_password(UserChangeForm):


  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
 )

  class Meta:
    model=User
    fields=["email", "first_name", "last_name"]

  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  def clean_password2(self):

    print(self.cleaned_data)

    password1 = self.cleaned_data["password1"]
    password2 = self.cleaned_data["password2"]

    if password1 != password2:
      raise forms.ValidationError("Las contraseñas deben ser iguales")
    return password2
  

  