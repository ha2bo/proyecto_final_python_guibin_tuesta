from django import forms
from .models import Sede, usuarios_gimnasio

class MiFormulario(forms.Form):
    sedes_select = forms.ModelMultipleChoiceField(
    queryset=Sede.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    )



class UsuarioFormulario(forms.ModelForm):

  class Meta:
    model= usuarios_gimnasio
    #fields=('__all__')
    fields=["nombre", "correo", "Telefono"]