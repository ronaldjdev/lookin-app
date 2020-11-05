from apps.login.forms import RegistryForms
from django.shortcuts         import render      , redirect
from django.http              import HttpResponse
from django.views    .generic import TemplateView, CreateView
from apps.user.models import Usuarios
from apps.stock.forms import InmuebleForm



class IndexCreateView(CreateView):
    model = Usuarios
    form_class = InmuebleForm
    template_name = "index.html"


class IndexView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "info/contact.html"


class AboutView(TemplateView):
    template_name = "info/about.html"




