from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from m7_python.models import Comuna, Region, Inmuebles, SolicitudInmueble

class UserForm(UserCreationForm):
  first_name = forms.CharField(label="Nombre", max_length=20)
  last_name = forms.CharField(label="Apellido", max_length=20)
  email = forms.EmailField(label="Correo")
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class TipoForm(forms.Form):
  tipos = ((1,'Arrendatario'), (2, 'Arrendador'))
  tipo = forms.ChoiceField(label="Tipo", choices=tipos)
  rut = forms.CharField(label='Rut', max_length=100)
  direccion = forms.CharField(label = 'Dirección', max_length=100)
  telefono = forms.CharField(label = 'Teléfono', max_length=100)

class UserUpdateForm(forms.ModelForm):
  class Meta:
    model=User
    fields=['first_name', 'last_name', 'email']
    labels = {
      'email': 'Correo'
    }

class InmuebleForm(forms.Form):
  tipos = ((1, "Casa"), (2, "Departamento"), (3, "Parcela"))
  id_tipo_inmueble = forms.ChoiceField(choices=tipos)
  comunas = [(x.id, x.comuna) for x in list(Comuna.objects.all())]
  comunas.sort(key=lambda a: a[1])
  regiones = [(x.id, x.region) for x in list(Region.objects.all())]

  id_comuna = forms.ChoiceField(choices=comunas)
  id_region = forms.ChoiceField(choices=regiones)
  nombre_inmueble = forms.CharField(label='Nombre Inmueble', max_length=100)
  descripcion = forms.CharField(label='Descripción', max_length=100)
  m2_construido = forms.FloatField(label='M2 construidos')
  m2_terreno = forms.FloatField(label='M2 terreno')
  numero_banos = forms.IntegerField(label="Núm. de baños")
  numero_est = forms.IntegerField(label="Núm. de estacionamientos")
  numero_hab = forms.IntegerField(label="Núm. de habitaciones")
  direccion = forms.CharField(label="Dirección", max_length = 40)

class InmueblesUpdateForm(forms.ModelForm):
  class Meta:
    model = Inmuebles
    fields = ['nombre_inmueble', 'descripcion', 'm2_construido', 'numero_banos', 'numero_hab', 'numero_est', 'direccion', 'm2_terreno']

class SelectorComuna(forms.Form):
  selector_comuna = forms.ModelChoiceField(queryset=Comuna.objects.all().order_by('comuna'), to_field_name='id', label="Comuna", widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Todas")