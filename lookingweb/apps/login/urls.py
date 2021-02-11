from django .urls                      import path, re_path
from django .contrib. auth .decorators import login_required
from django .conf                      import settings
from django .conf   .urls.static       import static
from        .views                     import *

'''-----------------------------------------------------------
Urls de identificacion para iniciar sesion, registros y de mas 
--------------------------------------------------------------'''
urlpatterns = [
    re_path(r'^log-in'          , LoginView         .as_view     (        ), name= 'log-in'          ),
    re_path(r'^log-out'         , login_required    (logout_page          ), name= 'log-out'         ),
    re_path(r'^sign-in'        , RegistrarUsuarios. as_view     (        ), name= 'sign-in'        ),
    re_path(r'^reset_password' , ResetPasswordView. as_view    (         ), name= 'reset_password' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)