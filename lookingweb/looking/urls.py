"""looking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from apps.user.models import Usuarios
from django .contrib              import admin
from django .conf                 import settings
from django .urls                 import path , include, re_path
from django .conf    .urls.static import static
from apps.home.views import IndexCreateView
from apps.user.views import UserPersonalView

urlpatterns = [

    path('admin/', admin.site.urls),

    #================================================================
    #                        INICIO
    #================================================================
    
    re_path(r'^$', IndexCreateView.as_view(),name = "index.html" ),
    
    #================================================================
    #                        URLs INFORMACION
    #================================================================
    
    re_path(r'^info/' , include(('apps.home.urls')) ),

    #================================================================
    #                        URLs SESION
    #================================================================
    
    re_path(r'^account/', include(('apps.login.urls')) ),

    #================================================================
    #                        URLs USUARIO
    #================================================================
    
    # Editar Informacion personal
    re_path(r'^users/<username>/', include(('apps.user.urls')) ),
    #path('users/<username>/user-personal/<pk>/' , UserPersonalView .as_view(), name   ='user-personal' ),
    
    # Perfiles de Agentes Inmobiliarios

    #================================================================
    #                        URLs INMUEBLES
    #================================================================
    
    # Agregar inmuebles
    re_path(r'^stock/',include(('apps.stock.urls')) ),
    

    #================================================================
    #                        URLs BLOGs
    #================================================================
    
    # Visualizar Blog informativo
    re_path(r'^blog/',include(('apps.blog.urls')) ),

    #================================================================
    #                        URLs SESION
    #================================================================
    
    # Errores
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)