from django import forms
from .models import Sede

class MiFormulario(forms.Form):
    sedes_select = forms.ModelMultipleChoiceField(
    queryset=Sede.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    )