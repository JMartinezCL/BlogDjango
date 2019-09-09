from django.urls import path
from . import views



urlpatterns = [
   path('usuario/registro/', views.registro, name='usuario'),
   path('usuario/login/', views.login),
   path('logout', views.logout),
]