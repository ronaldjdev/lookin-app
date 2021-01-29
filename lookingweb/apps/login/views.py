from django.shortcuts                   import render
from django.http                        import HttpResponse     ,HttpResponseRedirect
from django.urls                        import reverse_lazy
from django.utils     .decorators       import method_decorator
from django.views     .decorators.cache import never_cache
from django.views     .decorators.csrf  import csrf_protect
from django.views     .generic.edit     import FormView
from django.views     .generic          import TemplateView     , CreateView, ListView, UpdateView, DeleteView
from django.contrib   .auth             import authenticate     , login, logout
from apps  .user      .models           import Usuarios
from       .forms                       import LoginForms       , RegistryForms


"""
------------------------------------------------------
Modificaciones informacion personal cuenta de usuario 
------------------------------------------------------ 
"""

# Inicio de sesion

class LoginView (FormView):
    template_name = 'account/sign-in.html'
    form_class = LoginForms
    success_url = reverse_lazy('index')

    # Proteccion de peticiones  
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        '''Recoge el metodo del formulario'''
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

            
    # Validacion de formularios
    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(LoginView, self).form_valid(form)

# Finalizamos la sesión    

def logout_page(request):
    logout(request)
    return HttpResponseRedirect ('login')

# Registros de usuarios 
class RegistrarUsuarios (CreateView):
    model = Usuarios
    form_class = RegistryForms
    template_name = 'account/registro_form.html'
    success_url = reverse_lazy('index')


# Restablecer contraseña
class ResetPassword(TemplateView):
    template_name = "reset_password.html"


# Vista de precios
class PricingView(TemplateView):
    template_name = "pricing.html"







# Lista de usuarios
class ListarUsuarios(ListView):
    model = Usuarios
    template_name = "userList.html"

    def get_queryset(self):
        return self.model.objects.filter(activeUser=True)


# Borrar Usuarios
class EliminarUsuarios(DeleteView):
    model = Usuarios
    template_name = "userDelete.html"

# Opciones de cuenta 
class AccountView(TemplateView):
    template_name = "account/account.html"

# Modificacion de info Usuario
class UserUpdateView(TemplateView):
    model = Usuarios
    template_name = "account/user-personal.html"



