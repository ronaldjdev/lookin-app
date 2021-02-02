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

from django .contrib import admin
from django .urls    import path , include


urlpatterns = [

    path('admin/', admin.site.urls),

    #================================================================
    #                        INICIO
    #================================================================
    
    path(''    ,include(('apps.home.urls' ,'index' )) ),
    path('404' ,include(('apps.home.urls' ,'404'   )) ),

    #================================================================
    #                        URLs INFORMACION
    #================================================================
    
    path('info/' ,include(('apps.home.urls','about'  )) ),
    path('info/' ,include(('apps.home.urls','contact')) ),
    path('info/' ,include(('apps.home.urls','pricing')) ),
    path('info/' ,include(('apps.home.urls','warning')) ),

    #================================================================
    #                        URLs SESION
    #================================================================
    
    path('account/', include(('apps.login.urls','login'          )) ),
    path('account/', include(('apps.login.urls','logout'         )) ),
    path('account/', include(('apps.login.urls','sign-in'        )) ),
    path('account/', include(('apps.login.urls','reset-password' )) ),

    #================================================================
    #                        URLs USUARIO
    #================================================================
    
    # Editar Informacion personal
    path('user/', include(('apps.user.urls','account')) ),
    path('user/', include(('apps.user.urls','user-notification')) ),
    path('user/', include(('apps.user.urls','user-payment'     )) ),
    path('user/', include(('apps.user.urls','user-personal'    )) ),
    path('user/', include(('apps.user.urls','user-privacy'     )) ),
    path('user/', include(('apps.user.urls','user-security'    )) ),
    path('user/', include(('apps.user.urls','user-settings'    )) ),
    
    # Perfiles de Agentes Inmobiliarios
    path('agents/',include(('apps.user.urls' ,'agent-single')) ),
    path('agents/',include(('apps.user.urls' ,'agents-grid' )) ),

    #================================================================
    #                        URLs INMUEBLES
    #================================================================
    
    # Agregar inmuebles
    path('stock/',include(('apps.stock.urls','add-property'  )) ),
    path('stock/',include(('apps.stock.urls','add-property-1')) ),
    path('stock/',include(('apps.stock.urls','add-property-2')) ),
    path('stock/',include(('apps.stock.urls','add-property-3')) ),
    path('stock/',include(('apps.stock.urls','add-property-4')) ),
    path('stock/',include(('apps.stock.urls','add-property-5')) ),
    
    # Visualizar inmuebles
    path('/stock/',include(('apps.stock.urls','property-grid'  )) ),
    path('stock/',include(('apps.stock.urls','property-single')) ),


    #================================================================
    #                        URLs BLOGs
    #================================================================
    
    # Visualizar Blog informativo
    path('blog/',include(('apps.blog.urls','blog-grid'  )) ),
    path('blog/',include(('apps.blog.urls','blog-single')) ),

    #================================================================
    #                        URLs SESION
    #================================================================
    
    # Errores
]
