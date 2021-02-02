from django.shortcuts          import render
from django.views     .generic import ListView, DeleteView, TemplateView, UpdateView
from       .models             import Usuarios

# Create your views here.

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
    template_name = "users/account.html"

# Modificacion de info Usuario
class UserUpdateView(TemplateView):
    model = Usuarios
    template_name = "users/user-personal.html"

"""
====================================================================
        Modificaciones informacion personal cuenta de usuario 
==================================================================== 
"""

class UserSecurityView(TemplateView):
    template_name = "users/user-security.html"

class UserNotificationView(TemplateView):
    template_name = "users/user-notification.html"

class UserSettingsView(TemplateView):
    template_name = "users/user-settings.html"

class UserPrivacyView(TemplateView):
    template_name = "users/user-privacy.html"

class UserPaymentView(TemplateView):
    template_name = "users/user-payment.html"

"""
====================================================================
        Perfiles de informacion agentes inmobiliarios
==================================================================== 
"""

class AddAgentSingleView(TemplateView):
    template_name = "agents/agent-single.html"

class AddAgentGridView(TemplateView):
    template_name = "agents/agents-grid.html"