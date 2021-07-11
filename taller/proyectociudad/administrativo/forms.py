from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo_edificio']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese la dirección por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
        }



class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_prop', 'costo_depart', 'numero_cuartos', 'edificio']

    

class EdificioDepartamentoForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(EdificioDepartamentoForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombre_prop', 'costo_depart', 'numero_cuartos', 'edificio']
        
   