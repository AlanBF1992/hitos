from m7_python.models import *

def get_all_inmuebles():
  inm = Inmuebles.objects.all()
  return inm

def agregar_inmueble(data):
  id_user = data['id_user']
  id_tipo_inmueble = data['tipo_inm']
  nombre = data['nombre']
  descripcion = data['desc']
  m2_cons = data['m2_cons']
  num_ban = data['num_ban']
  num_hab = data['num_hab']
  direccion = data['direc']
  id_comuna = data['id_comuna']
  id_region = data['id_region']

  inm = Inmuebles.objects.create(
    id_user = id_user,
    id_tipo_inmueble = id_tipo_inmueble,
    id_comuna = id_comuna,
    id_region = id_region,
    nombre_inmueble = nombre,
    descripcion = descripcion,
    m2_construido = m2_cons,
    numero_banos = num_ban,
    numero_hab = num_hab,
    direccion = direccion
  )
  inm.save()

def actualizar_descripcion(inmueble_id, nueva_descripcion):
  inm = Inmuebles.objects.get(pk = inmueble_id)
  inm.descripcion = nueva_descripcion
  inm.save()

def eliminar_inmueble(inmueble_id):
  inm = Inmuebles.objects.get(pk = inmueble_id)
  inm.delete()