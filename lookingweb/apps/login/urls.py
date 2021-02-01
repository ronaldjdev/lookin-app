from django.urls        import path
from django .contrib.       auth  .decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from apps  .login.views import *

'''-----------------------------------------------------------
Urls de identificacion para iniciar sesion, registros y de mas 
--------------------------------------------------------------'''
urlpatterns = [
    path('login'  , LoginView        .as_view    (         ), name= 'login'  ),
    path('logout' , login_required   (logout_page          ), name= 'logout' ),
    path('account', login_required   (AccountView.as_view()), name= 'account'),
    path('sign-in', RegistrarUsuarios.as_view    (         ), name= 'sign-in'),
    path('reset_password', ResetPasswordView.as_view(), name= 'reset_password')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)