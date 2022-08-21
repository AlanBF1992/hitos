from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('', views.indexView, name = 'home'),
  path('login/', LoginView.as_view(next_page = 'dashboard_url'), name = 'login_url'),
  path('logout/', LogoutView.as_view(next_page = 'home'), name = 'logout_url'),
  path('register/', views.registerView, name = 'register_url'),
  path('register_tipo/', views.register_tipoView, name = 'register_tipo_url'),
  path('dashboard/', views.dashboardView, name = 'dashboard_url'),
  path('update_profile/', views.update_profileView, name = 'update_profile_url'),
  path('new_inmueble/', views.new_inmuebleView, name='new_inmueble_url'),
  path('update_inmueble/', views.inmuebles_updateView, name='update_inmueble_url'),
  path('eliminar_inmueble/', views.inmuebles_delete, name='eliminar_inmueble_url'),
  path('solicitar_inmueble/', views.solicitar_inmueble, name='solicitar_inmueble_url'),
  path('solicitudes/', views.solicitudesView, name="solicitudes_url"),
  path('desestimar_solicitud/', views.desestimar_solicitud, name="desestimar_solicitud_url"),
]