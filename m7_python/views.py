from django.shortcuts import render, redirect
from m7_python.services import *
from m7_python.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerView(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/register_tipo?user='+str(form.cleaned_data['username']))
  else:
    form = UserForm()
  
  return render(request, 'registration/register.html', {'form': form})

def register_tipoView(request):
  username = request.GET['user']
  if request.method == 'POST':
    form = TipoForm(request.POST)
    if form.is_valid():
      tipo = form.cleaned_data['tipo']
      rut = form.cleaned_data['rut']
      direccion = form.cleaned_data['direccion']
      telefono = form.cleaned_data['telefono']
      user = User.objects.get(username=username)
      tipo_user = Tipo_user.objects.get(id=int(tipo))
      datos = Profile(user=user, id_tipo_user=tipo_user, rut=rut, direccion=direccion, telefono=telefono)
      datos.save()
      return redirect('login_url')
  else:
    form = TipoForm()
  return render(request, 'registration/register_tipo.html', {'form': form})

@login_required
def dashboardView(request):
  current_user = request.user
  inm = Inmuebles.objects.filter(id_user_id=current_user.id).select_related('id_tipo_inmueble')
  return render(request, 'dashboard.html',{'inmuebles': inm})

def indexView(request):
  inmuebles = Inmuebles.objects.all()
  solicitudes = []
  if request.method == 'POST':
    form = SelectorComuna(request.POST)
    comuna_buscada = request.POST.get('selector_comuna')
    if comuna_buscada != "":
      inmuebles = inmuebles.filter(id_comuna=comuna_buscada)
  else:
    form = SelectorComuna()
  if request.user.is_authenticated:
    solicitudes = SolicitudInmueble.objects.filter(id_user = request.user).values_list('id_inmueble', flat=True)
      
  return render(request, 'index.html', {'inmuebles': inmuebles, 'titulo': 'Inicio', 'form': form, 'solicitudes': solicitudes})

@login_required
def update_profileView(request):
  if request.method == 'POST':
    form = UserUpdateForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('dashboard_url')
  else:
    form = UserUpdateForm(instance=request.user.profile)
    
  return render(request, 'registration/update_profile.html', {'form': form})

@login_required
def new_inmuebleView(request):
  if request.method == 'POST':
    form = InmuebleForm(request.POST)
    if form.is_valid():
      id_tipo_inmueble = form.cleaned_data['id_tipo_inmueble']
      id_comuna = form.cleaned_data['id_comuna']
      id_region = form.cleaned_data['id_region']
      nombre_inmueble = form.cleaned_data['nombre_inmueble']
      descripcion = form.cleaned_data['descripcion']
      m2_construido = form.cleaned_data['m2_construido']
      m2_terreno = form.cleaned_data['m2_terreno']
      numero_banos = form.cleaned_data['numero_banos']
      numero_est = form.cleaned_data['numero_est']
      numero_hab = form.cleaned_data['numero_hab']
      direccion = form.cleaned_data['direccion']

      tipo_inmueble = Tipo_inmueble.objects.get(id=int(id_tipo_inmueble))
      comuna = Comuna.objects.get(id=id_comuna)
      region = Region.objects.get(id=id_region)

      current_user = request.user
      #user = User.objects.get(id=current_user.id)

      inm = Inmuebles(
        id_tipo_inmueble = tipo_inmueble,
        id_comuna = comuna,
        id_region = region,
        nombre_inmueble = nombre_inmueble,
        descripcion = descripcion,
        m2_construido = m2_construido,
        m2_terreno = m2_terreno,
        numero_banos = numero_banos,
        numero_est = numero_est,
        numero_hab = numero_hab,
        direccion = direccion
      )

      inm.id_user_id = current_user.id
      inm.save()
      return redirect('dashboard_url')
  else:
    form = InmuebleForm()

  return render(request, 'new_inmueble.html', {'form': form})


@login_required
def inmuebles_updateView(request):
  inmueble_id = request.GET['id_inmueble']
  inmueble = Inmuebles.objects.get(id=inmueble_id)
  if request.method == 'POST':
    form = InmueblesUpdateForm(request.POST, instance=inmueble)
    if form.is_valid():
      form.save()
      return redirect('dashboard_url')
  else:
    form = InmueblesUpdateForm(instance=inmueble)

  return render(request, 'registration/update_profile.html', {'form': form})

@login_required
def inmuebles_delete(request):
  inmueble_id = request.GET['id_inmueble']
  inmueble = Inmuebles.objects.get(id=inmueble_id)
  inmueble.delete()
  return redirect('dashboard_url')

@login_required
def solicitar_inmueble(request):
  inmueble_id = request.GET['id_inmueble']
  print(inmueble_id)
  inmueble = Inmuebles.objects.get(pk = inmueble_id)
  usuario_id = request.GET['id_usuario']
  print(usuario_id)
  usuario = User.objects.get(pk = usuario_id)
  solicitud = SolicitudInmueble.objects.create(id_user = usuario, id_inmueble = inmueble)
  solicitud.save()
  return redirect('home')

@login_required
def solicitudesView(request):
  usuario = request.user.id
  solicitudes = SolicitudInmueble.objects.select_related('id_inmueble').select_related('id_inmueble__id_user').filter(id_inmueble__id_user = usuario)
  return render(request, 'solicitudes.html', {'solicitudes': solicitudes, 'usuario': usuario})
  
@login_required
def desestimar_solicitud(request):
  solicitud_id = request.GET['id_solicitud']
  solicitud = SolicitudInmueble.objects.get(id=solicitud_id)
  solicitud.delete()
  return redirect('dashboard_url')