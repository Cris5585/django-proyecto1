from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hola-mundo/', views.hola_mundo, name='hola_mundo'),
    path('crear-usuario/<str:nombre>', 
         views.crear_usuario, name='crear-usuario'),
    path('listar-usuarios/', views.listar_usuarios, name='listar-usuarios'),
]
