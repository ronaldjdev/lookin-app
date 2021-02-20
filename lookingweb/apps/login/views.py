from django.shortcuts                   import render               , redirect
from django.http                        import HttpResponseRedirect
from django.urls                        import reverse_lazy
from django.contrib   .auth             import authenticate, login                , logout
from django.contrib   .auth.models      import User
from django.utils     .decorators       import method_decorator
from django.views     .decorators.cache import never_cache
from django.views     .decorators.csrf  import csrf_protect
from django.views     .generic.edit     import FormView
from django.views     .generic          import TemplateView         , CreateView
from       .forms                       import LoginForms           , RegistrationForms


"""
------------------------------------------------------
Modificaciones informacion personal cuenta de usuario 
------------------------------------------------------ 
"""

# Inicio de sesion

class LoginView (FormView):
    template_name = 'account/log-in.html'
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
    return HttpResponseRedirect ('log-in')

# Registros de usuarios 
class RegisterUsers (CreateView):
    model = User
    form_class = RegistrationForms
    template_name = 'account/registration-forms.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password2')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('index') 



""""
    def form_valid(self, form):
        ''' Validamos el formulario'''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password2')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('index')
"""

# Restablecer contraseña
class ResetPasswordView(TemplateView):
    template_name = "account/reset_password.html"




