from django.urls import path
from app_cad_ususuarios import views

urlpatterns = [
    # rota , view resposável, nome de referência
    # usuarios.com
    
    path('',views.home,name='home'),
     # usuarios.com/usuarios
        path('usuarios',views.usuarios,name='listagem_usuarios'),
    
]
