from django.shortcuts         import render
from django.views    .generic import ListView, DeleteView, TemplateView, UpdateView
from       .models            import Usuarios

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
    template_name = "account/account.html"

# Modificacion de info Usuario
class UserUpdateView(TemplateView):
    model = Usuarios
    template_name = "account/user-personal.html"

"""
------------------------------------------------------
Modificaciones informacion personal cuenta de usuario 
------------------------------------------------------ 
"""

class UserSecurityView(TemplateView):
    template_name = "account/user-security.html"
